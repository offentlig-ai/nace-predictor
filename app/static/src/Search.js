import React from 'react'
import Downshift from 'downshift'
import { throttle, debounce } from "throttle-debounce"

export default class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            items: [],
            nace: []
        };
        this.autocompleteSearchDebounced = debounce(500, this.autocompleteSearch);
        this.autocompleteSearchThrottled = throttle(500, this.autocompleteSearch);
    }

    _autocompleteCache = {};

    componentWillMount() {
        import('./nace_beskrivelse.json').then(
          res => this.setState({ nace: res })
        );
    }

    onChange = (selection) => {
        console.log(`You selected ${selection.value}`)
    }

    onInputValueChange = (inputValue) => {
      console.log(`Input value ${inputValue}`)
      if (inputValue.length < 5 || inputValue.endsWith(' ')) {
        this.autocompleteSearchThrottled(inputValue);
      } else { 
        this.autocompleteSearchDebounced(inputValue);
      }
    }

    autocompleteSearch = (q) => {
        const url = window.location.href + 'api?q=' + q
        console.log(`url: ${url}`)
        const cached = this._autocompleteCache[url];
        if (cached) {
          return Promise.resolve(cached).then(results => {
                this.setState({items: results});
            });
        }

        this.waitingFor = q;
        fetch(url)
            .then(response => {
            if (response.status === 200) {
                if (q === this.waitingFor) {
                    response.json()
                    .then(results => {
                        this.setState({items: results});
                    })
                }
            }
        })
    }

    itemToString = (item) => {
        const {nace} = this.state;
        const entry = nace.filter(function(o) {
            return o.nace === item.nace;
        });

        return item.nace + ': ' + entry[0].tekst;
    }

    render() {

        const {items} = this.state;

        return (
            <div>
                <Downshift
                    onChange={selection => this.onChange(selection)}
                    onInputValueChange={(inputValue) => this.onInputValueChange(inputValue)}
                    itemToString={item => (item ? item.pred + ' ' + item.value : '')}
                    >
                    {({
                        getInputProps,
                        getItemProps,
                        getLabelProps,
                        getMenuProps,
                        isOpen,
                        inputValue,
                        highlightedIndex,
                        selectedItem,
                    }) => (
                       <div>
                        <label {...getLabelProps()}></label>
                        <input {...getInputProps(
                        {
                            style: {
                            fontSize: '1.2em',   
                            },
                        })} />
                        <ul {...getMenuProps()}>
                            {isOpen
                            ? items
                                .map((item, index) => (
                                    <li
                                    {...getItemProps({
                                        key: index,
                                        index,
                                        item,
                                        style: {
                                        listStyleType: 'none',
                                        fontSize: '1.2em',   
                                        backgroundColor:
                                            highlightedIndex === index ? 'darkgray' : 'black',
                                        fontWeight: selectedItem === item ? 'bold' : 'normal',
                                        },
                                    })}
                                    >
                                    {this.itemToString(item)}
                                    </li>
                                ))
                            : null}
                        </ul>
                        </div>
                    )}
                    </Downshift>
                </div>
        )}
}


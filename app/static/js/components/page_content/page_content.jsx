import React from 'react';
import ReactDOM from 'react-dom';

import Event from './event.jsx'

import "./page_content.css"

class LeftContent extends React.Component {
    render () {

        return (
           <div id="content-left">
           </div>
        )
    }
}

class CenterContent extends React.Component {
    render () {
        let events = [1, 2, 3, 4, 5, 6, 7];

        return (
           <div id="content-center">
                {events.map(val =>
                        <Event eventId={val} key={val} />
                )}
           </div>
        )
    }
}

class RightContent extends React.Component {
    render () {

        return (
           <div id="content-right">
           </div>
        )
    }
}

class PageContent extends React.Component {
    render() {
        return (
            <div id="page-content">
                <LeftContent />
                <CenterContent />
                <RightContent />
            </div>
        )
    }
}

export default PageContent;
import React from 'react';
import ReactDOM from 'react-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFire, faGlobe, faUserFriends, faBell } from '@fortawesome/free-solid-svg-icons'

import "./navbar.css"

class LeftSegment extends React.Component {
    render () {
        return (
            <ul id="navbar-left">
                <li id="banner">Slacl</li>
            </ul>
        )
    }
}

class MiddleSegment extends React.Component {
    render () {
        return (
            <ul id="navbar-middle">
                <li className="selected"><FontAwesomeIcon className="icon" icon={faFire} /></li>
                <li><FontAwesomeIcon className="icon" icon={faGlobe} /></li>
                <li><FontAwesomeIcon className="icon" icon={faUserFriends} /></li>
            </ul>
        )
    }
}

class RightSegment extends React.Component {
    render () {
        return (
            <ul id="navbar-right">
                <li><img className="icon" src="https://scontent.ffcm1-2.fna.fbcdn.net/v/t1.6435-1/cp0/p50x50/61787536_2263405003872267_4864331250501943296_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=7206a8&_nc_ohc=JrWqe1JGqYgAX-Uo-sv&_nc_ht=scontent.ffcm1-2.fna&oh=09d03f62b24b01e84dbb0ff78026e022&oe=60EF559E" /></li>
                <li><FontAwesomeIcon className="icon" id="notifications" icon={faBell} /></li>
            </ul>
        )
    }
}

class NavBar extends React.Component {
    
    render() {
        return (
            <div role="navigation" id="navbar">
                <LeftSegment />
                <MiddleSegment />
                <RightSegment />
            </div>
        )
    }
} 


export default NavBar;
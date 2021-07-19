import React from 'react';
import ReactDOM from 'react-dom';

import "./event.css"

class Event extends React.Component {
    render() {
        return (
            <div className="event">
                <div className="event-header">
                    <div className="event-title">
                        Lorem Ipsum
                    </div>
                </div>
                <div className="event-content">
                    <p className="event-body">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas non magna arcu. Nam tempus, lorem vitae sollicitudin volutpat, dolor arcu convallis justo, in porttitor libero odio ac leo. Sed nisl elit, porta eu ullamcorper vel, lobortis at ipsum. Sed vel pharetra erat. Nulla venenatis eleifend enim ut dictum. Praesent vel auctor nibh, sit amet pretium nulla. Pellentesque at leo ut orci rhoncus scelerisque vel non orci. Maecenas et augue quam. Sed iaculis lacus in lacus venenatis vehicula.

Nunc in est a dui auctor feugiat mattis non nunc. Mauris mauris est, rhoncus posuere rutrum vitae, convallis a urna. Etiam volutpat urna commodo sem vestibulum, sed sagittis sem rhoncus. Nam tellus odio, hendrerit vitae volutpat et, sagittis semper nibh. Mauris interdum a augue ac tempor. Nulla eu elementum lorem. Nunc efficitur, urna sed aliquam convallis, purus justo lobortis leo, sit amet aliquam turpis elit sit amet sapien. Fusce eu massa elit. Donec ut feugiat elit, in facilisis tellus. Aliquam tellus quam, congue sit amet magna vel, hendrerit porta felis. Aenean vestibulum, felis sit amet suscipit tempor, sem ipsum tincidunt risus, id rhoncus ligula justo eget felis. Phasellus consectetur a nunc a interdum. Vestibulum eu nibh massa. Duis at risus nec nulla laoreet finibus vitae sit amet sapien.
                    </p>
                </div>
            </div>
        )
    }
}

export default Event;

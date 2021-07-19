import React from 'react';
import ReactDOM from 'react-dom';
import NavBar from "./components/navbar/navbar.jsx"
import PageContent from "./components/page_content/page_content.jsx"

import "./index.css"
import "./normalize.css"
/*
 * TODO: write app
 */

 ReactDOM.render(
     <React.Fragment>
         <NavBar />
         <PageContent />
     </React.Fragment>,
     document.getElementById('react-entrypoint')
 )

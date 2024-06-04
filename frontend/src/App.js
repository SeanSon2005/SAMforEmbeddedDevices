import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes, Navigate } from 'react-router-dom';
import Home from './Home'
import Logout from './Logout';
import Profile from './Profile';
import Datasets from './Datasets';
import DatasetDetail from './DatasetDetail';
import DatasetCreate from './DatasetCreate';
import DatasetDelete from './DatasetDelete';
import DatasetUpload from './DatasetUpload';
import './global.css';

const App = () => {
    return (
        <Router>
            <div>
                <nav className="navbar">
					<div className="logo">ObjdumpAI</div>
                    <ul className="nav-links">
						<li><Link to="/">Home</Link></li>
                        <li><Link to="/profile">Profile</Link></li>
                        <li><Link to="/datasets">Datasets</Link></li>
                        <li><Link to="/logout">Logout</Link></li>
                    </ul>
                </nav>
                <Routes>
					<Route path="/" element={<Home />} />
                    <Route path="/logout" element={<Logout/>} />
                    <Route path="/profile" element={<Profile/>} />
                    <Route path="/datasets" element={<Datasets/>} />
					<Route path="/datasets/:datasetId" element={<DatasetDetail/>} />
					<Route path="/create" element={<DatasetCreate/>} />
					<Route path="/delete/:datasetId" element={<DatasetDelete/>} />
					<Route path="/upload/:datasetId" element={<DatasetUpload/>} />
					<Route path="*" element={<Navigate to="/" />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;

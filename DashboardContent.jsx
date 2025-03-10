import React, { useState, useEffect, useRef } from 'react';
import '../../Styles/DashboardContent.css';

const DashboardContent = () => {
    const [cameraStatus, setCameraStatus] = useState({});
    const camStatusRef = useRef(null); // Use ref instead of document.getElementById

    useEffect(() => {
        const fetchCameraStatus = async () => {
            try {
                const response = await fetch("http://localhost:5001/dashboard");
                const data = await response.json();
                setCameraStatus(data);

                if (camStatusRef.current) { // Check if ref exists before updating
                    camStatusRef.current.style.backgroundColor = data.status === "ONLINE" ? "red" : "green";
                }
            } catch (error) {
                console.error("Error fetching camera status:", error);
            }
        };

        fetchCameraStatus();
        const interval = setInterval(fetchCameraStatus, 5000); // Auto-refresh every 5 sec

        return () => clearInterval(interval);
    }, []); // No dependencies needed
    return (
        <div className="dashcont_container">
            <div className="camdetails">
                <div className="cam1">
                    <div className="camname_status">
                        <p>CAM_1</p>
                        <p ref={camStatusRef}>
                            {cameraStatus.CAM_1 ? cameraStatus.CAM_1.status : "Loading..."}
                        </p>                 </div>
                    <iframe id="web-container1" class="web-container"
                        src={cameraStatus.CAM_1 ? cameraStatus.CAM_1.url : ""}
                        title="Camera 1 Live Feed"
                        sandbox="allow-scripts allow-same-origin"
                        scrolling="no">
                    </iframe>
                </div>
                <div className="cam2">
                    <div className="camname_status">
                        <p>CAM_2</p>
                        <p ref={camStatusRef}>
                            {cameraStatus.CAM_2 ? cameraStatus.CAM_2.status : "Loading..."}
                        </p>                    </div>

                    <iframe id="web-container1" class="web-container"
                        src={cameraStatus.CAM_1 ? cameraStatus.CAM_1.url : ""}
                        title="Camera 2 Live Feed"
                        sandbox="allow-scripts allow-same-origin"
                        scrolling="no">
                    </iframe>
                </div>
            </div>
            <div className="secondrow">
                <div className="leftside_values">
                    <div className="top_content">
                        <div className="taprate">
                            <p>Tap Rate Kg/h</p>
                            <p>123.567</p>
                        </div>
                        <div className="highlow">
                            <p>HIGH</p>
                            <p>123.456</p>
                            <p>LOW</p>
                            <p>123.456</p>
                        </div>
                    </div>
                    <div className="bottom_content">
                        <div className="tap_value">
                            <p>Tap Rate kg/s</p>
                            <p>123.456</p>
                        </div>
                        <div className="bottom_value">
                            <p>Stream width (pixel) </p>
                            <p>123.456</p>
                            <p>Factor</p>
                            <p>123.456</p>
                        </div>
                    </div>
                </div>
                <div className="rightside_Values">
                    <div className="righttop_content">
                        <div className="stream_position">
                            <p>Stream Position (Pixel)</p>
                            <p>123.567</p>
                        </div>
                        <div className="highlow">
                            <p>HIGH</p>
                            <p>123.456</p>
                            <p>LOW</p>
                            <p>123.456</p>
                        </div>
                    </div>
                    <div className="bottom_output">
                        <p>alarm output</p>
                        <div className="indications">
                            <div className="tap">
                                <p></p>
                                <p>tap</p>
                            </div>
                            <div className="posi">
                                <p></p>
                                <p>posi</p>
                            </div>
                            <div className="alarmrdy">
                                <p></p>
                                <p>alarmrdy</p>
                            </div>
                            <div className="auto">
                                <p></p>
                                <p>auto</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="third_row">
                <div className="graph">
                    <p></p>
                </div>
            </div>
        </div>
    )
}

export default DashboardContent

// import React, { useEffect, useState } from "react";
// import "../../Styles/DashboardContent.css";

// const DashboardContent = () => {
//     const [cameraStatus, setCameraStatus] = useState({});

//     useEffect(() => {
//         const fetchCameraStatus = async () => {
//             try {
//                 const response = await fetch("http://localhost:5001/dashboard");
//                 const data = await response.json();
//                 setCameraStatus(data);
//             } catch (error) {
//                 console.error("Error fetching camera status:", error);
//             }
//         };

//         fetchCameraStatus();
//         const interval = setInterval(fetchCameraStatus, 5000); // Auto-refresh every 5 sec

//         return () => clearInterval(interval);
//     }, []);

//     return (
//         <div className="dashcont_container">
//             <div className="camdetails">
//                 <div className="cam1">
//                     <div className="camname_status camera_status">
//                         <p>CAM_1</p>
//                         <p>{cameraStatus.CAM_1 ? cameraStatus.CAM_1.status : "Loading..."}</p>
//                     </div>
//                     <iframe
//                         id="web-container1"
//                         className="web-container"
//                         src={cameraStatus.CAM_1 ? cameraStatus.CAM_1.url : ""}
//                         sandbox="allow-scripts allow-same-origin"
//                         title="Camera 1 Live Feed"  // Add a unique title
//                         // scrolling="no"
//                     />
//                 </div>
//                 <div className="cam2">
//                     <div className="camname_status camera_status">
//                         <p>CAM_2</p>
//                         <p>{cameraStatus.CAM_2 ? cameraStatus.CAM_2.status : "Loading..."}</p>
//                     </div>
//                     <img src={cameraStatus.CAM_2 ? cameraStatus.CAM_2.url : ""} alt="CAM_2" />
//                 </div>
//             </div>
//         </div>
//     );
// };


// import React, { useEffect, useState } from "react";
// import "../../Styles/DashboardContent.css";
// // import { faWifi3 } from "@fortawesome/free-solid-svg-icons";

// const DashboardContent = () => {
//     const [cameraStatus, setCameraStatus] = useState({});

//     useEffect(() => {
//         const fetchCameraStatus = async () => {
//             try {
//                 const response = await fetch("http://localhost:5001/dashboard");
//                 const data = await response.json();
//                 setCameraStatus(data);
//                 console.log(data)

//             } catch (error) {
//                 console.error("Error fetching camera status:", error);
//             }

//         };

//         fetchCameraStatus();
//         const interval = setInterval(fetchCameraStatus, 5000); // Refresh every 5 seconds

//         return () => clearInterval(interval);
//     }, []);

//     return (
//         <div className="dashcont_container">
//             <div className="camdetails">
//                 {/* Camera 1 */}
//                 <div className="camera-card">
//                     <div className="camname_status">
//                         <p>CAM_1</p>
//                         <span className={`status-indicator ${cameraStatus.CAM_1?.status === "ONLINE" ? "online" : "offline"}`}></span>
//                         <p>{cameraStatus.CAM_1 ? cameraStatus.CAM_1.status : "Loading..."}</p>
//                     </div>
//                     {/* <iframe
//                         className="camera-frame"
//                         title="Camera 1 Live Feed"
//                         src={cameraStatus.CAM_1 ? cameraStatus.CAM_1.url : ""}
//                         sandbox="allow-scripts "
//                         scrolling="no"
//                     /> */}
//                    <iframe src={cameraStatus.CAM_1 ? cameraStatus.CAM_1.url : "no"} frameborder="0" title="Camera 1 Live Feed"></iframe>
//                 </div>

//                 {/* Camera 2 */}
//                 <div className="camera-card">
//                     <div className="camname_status">
//                         <p>CAM_2</p>
//                         <span className={`status-indicator ${cameraStatus.CAM_2?.status === "ONLINE" ? "online" : "offline"}`}></span>
//                         <p>{cameraStatus.CAM_2 ? cameraStatus.CAM_2.status : "Loading..."}</p>
//                     </div>
//                     {/* <iframe
//                         className="camera-frame"
//                         title="Camera 2 Live Feed"
//                         src={cameraStatus.CAM_2 ? cameraStatus.CAM_2.url : ""}
//                         sandbox="allow-scripts "
//                         scrolling="no"
//                     /> */}
//                     <img src={cameraStatus.CAM_2 ? cameraStatus.CAM_2.url : ""} alt="" />
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default DashboardContent;

import React from 'react';

function ScannerPage() {
  const openFlaskModel = () => {
    window.open("http://127.0.0.1:5000/", "_blank"); // Opens Flask app in a new tab
  };

  return (
    <div>
      <h1>AI Model Scanner</h1>
      <button onClick={openFlaskModel}>Open AI Model</button>
    </div>
  );
}

export default ScannerPage;

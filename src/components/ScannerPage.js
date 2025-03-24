import React from 'react';

function ScannerPage() {
  const openFlaskModel = () => {
    window.open("https://7e50-136-233-11-130.ngrok-free.app", "_blank"); // Opens Flask app in a new tab
  };

  return (
    <div>
      <h1>AI Model Scanner</h1>
      <button onClick={openFlaskModel}>Open AI Model</button>
    </div>
  );
}

export default ScannerPage;

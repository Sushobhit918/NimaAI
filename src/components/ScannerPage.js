import React from 'react';

function ScannerPage() {
  const openFlaskModel = () => {
    window.open("https://5a99-2409-40d1-17-e49d-b041-3455-ff66-434d.ngrok-free.app", "_blank"); // Opens Flask app in a new tab
  };

  return (
    <div>
      <h1>AI Model Scanner</h1>
      <button onClick={openFlaskModel}>Open AI Model</button>
    </div>
  );
}

export default ScannerPage;

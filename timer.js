import React, { useState, useEffect } from 'react';
import './App.css'; // Import the CSS file

const Timer = () => {
  const [time, setTime] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    let timer;
    if (isRunning) {
      timer = setInterval(() => {
        setTime(prevTime => prevTime + 1);
      }, 1000);
    }
    return () => clearInterval(timer);
  }, [isRunning]);

  const startTimer = () => {
    setIsRunning(true);
  };

  const pauseTimer = () => {
    setIsRunning(false);
  };

  const resetTimer = () => {
    setIsRunning(false);
    setTime(0);
  };

  return (
    <div className="timer-container">
      <h1 className="timer-title">Timer</h1>
      <h2 className="timer-display">{time} seconds</h2>
      <div className="button-container">
        <button className="timer-button start" onClick={startTimer}>Start</button>
        <button className="timer-button pause" onClick={pauseTimer}>Pause</button>
        <button className="timer-button reset" onClick={resetTimer}>Reset</button>
      </div>
    </div>
  );
};

export default Timer;


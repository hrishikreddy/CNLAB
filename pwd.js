import React, { useState } from 'react';

const PasswordStrengthChecker = () => {
  const [password, setPassword] = useState('');
  const [strength, setStrength] = useState('');

  const checkPasswordStrength = (pwd) => {
    let strengthLevel = 0;

    // Conditions to check password strength
    if (pwd.length >= 8) strengthLevel += 1; // Length should be at least 8 characters
    if (/[A-Z]/.test(pwd)) strengthLevel += 1; // Contains at least one uppercase letter
    if (/[a-z]/.test(pwd)) strengthLevel += 1; // Contains at least one lowercase letter
    if (/[0-9]/.test(pwd)) strengthLevel += 1; // Contains at least one number
    if (/[^A-Za-z0-9]/.test(pwd)) strengthLevel += 1; // Contains at least one special character

    // Determine the password strength
    switch (strengthLevel) {
      case 0:
        setStrength('');
        break;
      case 1:
        setStrength('Very Weak');
        break;
      case 2:
        setStrength('Weak');
        break;
      case 3:
        setStrength('Moderate');
        break;
      case 4:
        setStrength('Strong');
        break;
      case 5:
        setStrength('Very Strong');
        break;
      default:
        setStrength('');
    }
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    checkPasswordStrength(e.target.value);
  };

  return (
    <div>
      <h2>Password Checker</h2>
      <input type="password" placeholder="Enter password" onChange={handlePasswordChange} />
      <p>{strength && `Strength: ${strength}`}</p>
    </div>
  );
}

export default PasswordStrengthChecker;

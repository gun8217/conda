import React from 'react';
import { TextField, StyledLabel } from '../../../styled/common_styled';  // styles.ts에서 가져오기

interface InputProps {
  label: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
  bgColor?: string;
}

const Input: React.FC<InputProps> = ({ label, value, onChange, placeholder, bgColor }) => {
  return (
    <div>
      <label>{label}</label>
      <TextField
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        bgColor={bgColor} // bgColor prop 전달
      />
    </div>
  );
};

export default Input;
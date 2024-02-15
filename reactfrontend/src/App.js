import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [students, setStudents] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
  });

  const getAllStudent = async () => {
    try {
      const students = await axios.get("http://127.0.0.1:8000/app/students/");
      setStudents(students.data);
      // console.log(students.data)
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getAllStudent();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // const handleSubmit = async (e) => {
  //   e.preventDefault();
  
  //   try {
  //     const response = await axios.post("http://127.0.0.1:8000/app/addStudent/", formData);
  //     console.log('POST request successful:', response.data);
  //     getAllStudent();
  //   } catch (error) {
  //     console.error(error);
  //   }
  // };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
  
    try {
      console.log('Form Data:', formData);
  
      const response = await axios.post("http://127.0.0.1:8000/app/addStudent/", {
        stname: formData.name,
        stemail: formData.email,
      });
      console.log('POST request successful:', response.data);
  
      getAllStudent();
    } catch (error) {
      console.error('Error making POST request:', error);
  
      // Log the detailed response content
      if (error.response) {
        console.error('Response data:', error.response.data);
        console.error('Response status:', error.response.status);
        console.error('Response headers:', error.response.headers);
      }
    }
  };
  
  

  return (
    <div className="App">
      <h1>Connect React JS to Django</h1>
      <h2>Submit Form to POST API:</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>

      <h2>Data from GET:</h2>
      {students.map((student, i) => (
        <div key={i}>
          <h2>ID: {student.id}</h2>
          <h2>Name: {student.stname}</h2>
          <h2>Email: {student.stemail}</h2>
        </div>
      ))}
    </div>
  );
}

export default App;

import logo from './logo.svg';
import './App.css';
import { useState,useEffect } from 'react';
import axios from 'axios';
function App() {
  const [students, setStudents] = useState([])
  useEffect (()=>{
  async function getAllStudent() {
    try {
        const students = await axios.get("http://127.0.0.1:8000/app/students/")
        console.log(students.data)
        setStudents (students.data)
      } catch (error) {
          console.log(error)
      }
    }
    getAllStudent()
  }, [])
  return (
    <div className="App">
      <h1>Connect React JS to Django</h1>
      <h2>Data :- </h2> 
      {
        students.map((student, i)=>{
          return (
            <h2 key={i}>ID : {student.id} <br />Name : {student.stname} <br />Email : {student.stemail}</h2>
          )
        }) 
      }
      
      </div>
  );
}

export default App;
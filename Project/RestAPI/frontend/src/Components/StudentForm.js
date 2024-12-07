import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';



function StudentForm() {
  const [students, setStudents] = useState([]);
  const [formData, setFormData] = useState({ id: '', name: '', age: '' });
  const [isEdit, setIsEdit] = useState(false);

  // Fetch all students
  const fetchStudents = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/all/');
      setStudents(response.data);
    } catch (error) {
      console.error('Error fetching students:', error);
    }
  };

  // Handle form input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Handle form submission (Create or Update)
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isEdit) {
        await axios.put('http://127.0.0.1:8000/api/all/', formData);
      } else {
        await axios.post('http://127.0.0.1:8000/api/all/', formData);
      }
      setFormData({ id: '', name: '', age: '' });
      setIsEdit(false);
      fetchStudents(); // Refresh student list
    } catch (error) {
      console.error('Error submitting formkn :', error);
    }
  };

  // Edit student
  const editStudent = (student) => {
    setFormData({ id: student.id, name: student.name, age: student.age });
    setIsEdit(true);
  };

  // Delete student
  const deleteStudent = async (id) => {
    try {
      await axios.delete('http://127.0.0.1:8000/api/all/', { data: { id } });
      fetchStudents();
    } catch (error) {
      console.error('Error deleting student:', error);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  return (
    <div className="container mt-5">
      <h2 className="mb-4">{isEdit ? 'Edit' : 'Add'} Student</h2>
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="mb-3">
          <label className="form-label">Name</label>
          <input
            type="text"
            name="name"
            className="form-control"
            placeholder="Enter student name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Age</label>
          <input
            type="number"
            name="age"
            className="form-control"
            placeholder="Enter student age"
            value={formData.age}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          {isEdit ? 'Update' : 'Add'} Student
        </button>
      </form>

      <h3>Students List</h3>
      <ul className="list-group">
        {students.map((student) => (
          <li key={student.id} className="list-group-item d-flex justify-content-between align-items-center">
            <span>
              name : {student.name} , age : {student.age}
            </span>
            <div>
              <button className="btn btn-sm btn-warning me-2" onClick={() => editStudent(student)}>
                Edit
              </button>
              <button className="btn btn-sm btn-danger" onClick={() => deleteStudent(student.id)}>
                X
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StudentForm;

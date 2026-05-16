import React, { useEffect, useState } from "react";

function UserForm() {

    // BACKEND URL
    const API_BASE = "https://react-django-fullstack-1.onrender.com";

    const [roles, setRoles] = useState([]);

    const [users, setUsers] = useState([]);

    const [formData, setFormData] = useState({
        email: "",
        first_name: "",
        last_name: "",
        empid: "",
        role_id: "",
        supervisor_email: ""
    });

    // FETCH ROLES + USERS
    useEffect(() => {
        fetchRoles();
        fetchUsers();
    }, []);

    // FETCH ROLES
    const fetchRoles = async () => {
        try {

            const response = await fetch(
                `${API_BASE}/api/roles/`
            );

            const data = await response.json();

            setRoles(data);

        } catch (error) {
            console.log("Roles Fetch Error:", error);
        }
    };

    // FETCH USERS
    const fetchUsers = async () => {
        try {

            const response = await fetch(
                `${API_BASE}/api/users/`
            );

            const data = await response.json();

            setUsers(data);

        } catch (error) {
            console.log("Users Fetch Error:", error);
        }
    };

    // HANDLE INPUT
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    // CREATE USER
    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            const response = await fetch(
                `${API_BASE}/api/users/create/`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(formData)
                }
            );

            const data = await response.json();

            alert(data.message);

            fetchUsers();

            setFormData({
                email: "",
                first_name: "",
                last_name: "",
                empid: "",
                role_id: "",
                supervisor_email: ""
            });

        } catch (error) {
            console.log("Create User Error:", error);
        }
    };

    return (

        <div style={{ padding: "30px" }}>

            <h2>User Creation</h2>

            <form onSubmit={handleSubmit}>

                <div>
                    <label>Email</label>
                    <br />

                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>

                <br />

                <div>
                    <label>First Name</label>
                    <br />

                    <input
                        type="text"
                        name="first_name"
                        value={formData.first_name}
                        onChange={handleChange}
                        required
                    />
                </div>

                <br />

                <div>
                    <label>Last Name</label>
                    <br />

                    <input
                        type="text"
                        name="last_name"
                        value={formData.last_name}
                        onChange={handleChange}
                        required
                    />
                </div>

                <br />

                <div>
                    <label>EMPID</label>
                    <br />

                    <input
                        type="text"
                        name="empid"
                        value={formData.empid}
                        onChange={handleChange}
                        required
                    />
                </div>

                <br />

                {/* ROLE DROPDOWN */}
                <div>

                    <label>Role</label>

                    <br />

                    <select
                        name="role_id"
                        value={formData.role_id}
                        onChange={handleChange}
                        required
                    >

                        <option value="">
                            Select Role
                        </option>

                        {roles.map((role) => (

                            <option
                                key={role.id}
                                value={role.id}
                            >
                                {role.role_type}
                            </option>

                        ))}

                    </select>

                </div>

                <br />

                <div>

                    <label>Supervisor Email</label>

                    <br />

                    <input
                        type="email"
                        name="supervisor_email"
                        value={formData.supervisor_email}
                        onChange={handleChange}
                    />

                </div>

                <br />

                <button type="submit">
                    Create User
                </button>

            </form>

            <hr />

            <h2>Users List</h2>

            <table border="1" cellPadding="10">

                <thead>

                    <tr>
                        <th>ID</th>
                        <th>Email</th>
                        <th>Name</th>
                        <th>Role</th>
                        <th>Supervisor_ID</th>
                    </tr>

                </thead>

                <tbody>

                    {users.map((user) => (

                        <tr key={user.id}>

                            <td>{user.id}</td>

                            <td>{user.email}</td>

                            <td>
                                {user.first_name} {user.last_name}
                            </td>

                            <td>
                                {user.role.role_type}
                            </td>

                            <td>
                                {
                                    user.supervisor
                                        ? user.supervisor.id
                                        : "No Supervisor"
                                }
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );
}

export default UserForm;
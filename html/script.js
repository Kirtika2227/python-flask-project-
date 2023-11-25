//const api_url = "<heroku_app_url>"
const api_url = " http://127.0.0.1:8080/students"
function loadData(records = []) {
    var table_data = "";
    for (let i = 0; i < records.length; i++) {
        table_data += `<tr>`;
        table_data += `<td>${records[i].student_id}</td>`;
        table_data += `<td>${records[i].name}</td>`;
        table_data += `<td>${records[i].email}</td>`;
        table_data += `<td>${records[i].phone}</td>`;
        table_data += `<td>${records[i].selected_course}</td>`;
        table_data += `<td>`;
        table_data += `<a href="edit.html?id=${records[i].student_id}"><button class="btn btn-primary">Edit</button></a>`;
        table_data += '&nbsp;&nbsp;';
        table_data += `<button class="btn btn-danger" onclick=deleteData('${records[i].student_id}')>Delete</button>`;
        table_data += `</td>`;
        table_data += `</tr>`;
    }
    //console.log(table_data);
    document.getElementById("tbody").innerHTML = table_data;
}
function getData() {
    fetch(api_url)
        .then((response) => response.json())
        .then((data) => {
            console.table(data);
            loadData(data);
        });
}
function getDataById(student_id) {
    fetch(`${api_url}/${student_id}`)
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            data = data[0]
            document.getElementById("student_id").value = data.student_id;
            document.getElementById("name").value = data.name;
            document.getElementById("email").value = data.email;
            document.getElementById("phone").value = data.phone;
            document.getElementById("selected_course").value = data.selected_course;
        })
}
function postData() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var selected_course = document.getElementById("selected_course").value;
    data = { name: name, email: email, phone: phone, selected_course: selected_course };
    fetch(api_url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            window.location.href = "index.html";
        })
}
function putData() {
    var student_id = document.getElementById("student_id").value;
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var selected_course = document.getElementById("selected_course").value;

    data = { student_id: student_id, name: name, email: email, phone: phone, selected_course: selected_course };
    console.log(data)
    fetch(api_url, {
        method: "PUT",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .then((data) => {
            console.table(data);
            window.location.href = "index.html";
        })
}
function deleteData(student_id) {
    user_input = confirm("Are you sure you want to delete this record?");
    if (user_input) {
        fetch(api_url, {
            method: "DELETE",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "student_id": student_id })
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                window.location.reload();
            })
    }
}

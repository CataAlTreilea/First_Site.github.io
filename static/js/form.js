function validateForm() {
    let firstName = document.getElementById("first_name").value;
    let lastName = document.getElementById("last_name").value;
    let email = document.getElementById("email").value;
    let phoneNumber = document.getElementById("phone_number").value;
    let dob = document.getElementById("dob").value;
    let country = document.getElementById("country").value;

    if (firstName == "" || lastName == "" || email == "" || phoneNumber == "" || dob == "" || country == "") {
        alert("All fields must be filled out");
        return false;
    }

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}

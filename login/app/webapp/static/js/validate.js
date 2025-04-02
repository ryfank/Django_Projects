function validatePassword() {
    var password = document.getElementById("pwd").value;
    var minLength = 10;
    var hasNumber = /\d/.test(password);
    var hasLetter = /[a-zA-Z]/.test(password);
    var hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    if (password.length < minLength) {
        alert("Password must be at least " + minLength + " characters long.");
    } else if (!hasNumber || !hasLetter || !hasSpecialChar) {
        alert("Password must contain at least one number, one letter, and one special character.");
    } else {
        alert("Password is valid!");
    }
}

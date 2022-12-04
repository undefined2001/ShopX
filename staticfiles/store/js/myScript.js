const icon = document.querySelector("#icon")
const pass = document.querySelector("#pass")

icon.addEventListener("click", function () {
    console.log(icon, pass)
    this.classList.toggle("fa-eye")
    this.classList.toggle("fa-eye-slash")
    const type = pass.getAttribute("type") === "password" ? "text" : "password";
    pass.setAttribute("type", type)
    console.log(type)
})
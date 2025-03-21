// DOM selector
const form = document.querySelector("form.login");
const tabContainer = document.querySelector(".tabs");
const tabs = document.querySelectorAll(".tab");
const studentTab = document.querySelector("#student-tab");
const parentTab = document.querySelector("#parent-tab");
const teacherTab = document.querySelector("#teacher-tab");
const studentForm = document.querySelector(".student-form");
const parentForm = document.querySelector(".parent-form");
const teacherForm = document.querySelector(".teacher-form");
const forms = document.querySelectorAll("[class *='-form']");
let userType = document.querySelector("#user_type");
const submitButton = document.querySelector(".submit")

// changer de formulaire selon le button cliqué
console.log(userType.value)
userType.value = ''
console.log(userType.value)
tabs.forEach((tab) => {
  tab.addEventListener("click", (e) => {
    resetActiveTab(tab);

    if (e.target == studentTab) {
      resetActiveForm(studentForm);
      userType.setAttribute("value" , "student");
      console.log(userType.value);

    }
    if (e.target == parentTab) {
      resetActiveForm(parentForm);
      userType.setAttribute("value" , "parent");
      console.log(userType.value);

    }
    if (e.target == teacherTab) {
      resetActiveForm(teacherForm);
      userType.setAttribute("value" , "teacher");
      console.log(userType.value);

    }
  });
});

// condition ? actions (si c'est vrai) : actions (si c'est pas vrai)
/* équivaut à
 si (conditions) {
  actions
 }
  
 */
// condition && actions (si c'est vrai)

// la fonction pour changer de changer le button actif

function resetActiveTab(tab) {
  tab.nextElementSibling
    ? tab.nextElementSibling.classList.remove("active")
    : tab.parentElement.firstElementChild.classList.remove("active");
  tab.previousElementSibling
    ? tab.previousElementSibling.classList.remove("active")
    : tab.parentElement.lastElementChild.classList.remove("active");
  if (!tab.classList.contains("active")) {
    tab.classList.add("active");
  }
}

// fonction pour changer le formulaire actif
function resetActiveForm(form) {
  if (form.nextElementSibling) {
    form.nextElementSibling.classList.remove("active");
    form.nextElementSibling.classList.add("hidden");
  } else {
    form.parentElement.firstElementChild.classList.remove("active");
    form.parentElement.firstElementChild.classList.add("hidden");
  }
  if (form.previousElementSibling) {
    form.previousElementSibling.classList.remove("active");
    form.previousElementSibling.classList.add("hidden");
  } else {
    form.parentElement.lastElementChild.classList.remove("active");
    form.parentElement.lastElementChild.classList.add("hidden");
  }
  if (!form.classList.contains("active")) {
    form.classList.remove("hidden");
    form.classList.add("active");
  }
}

form.addEventListener('submit', (e) => {
  e.preventDefault
  console.log(userType.value)
})


submitButton.addEventListener('click', (e) => {
  console.log(userType.value)
})


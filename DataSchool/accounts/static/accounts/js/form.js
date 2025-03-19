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
const submitButton = document.querySelector(".submit");

// Initialisation
console.log("Valeur initiale :", userType.value);
userType.value = ""; // Réinitialisation
console.log("Après reset :", userType.value);

// Fonction pour changer l'onglet actif
function resetActiveTab(tab) {
  tabs.forEach(t => t.classList.remove("active")); // Désactive tous les onglets
  tab.classList.add("active"); // Active celui qui est cliqué
}

// Fonction pour changer le formulaire actif
function resetActiveForm(form) {
  forms.forEach(f => {
    f.classList.remove("active");
    f.classList.add("hidden");
  });

  form.classList.remove("hidden");
  form.classList.add("active");
}

// Gestion du changement de formulaire
tabs.forEach((tab) => {
  tab.addEventListener("click", (e) => {
    resetActiveTab(tab);

    if (tab === studentTab) {
      resetActiveForm(studentForm);
      userType.value = "student";
    } else if (tab === parentTab) {
      resetActiveForm(parentForm);
      userType.value = "parent";
    } else if (tab === teacherTab) {
      resetActiveForm(teacherForm);
      userType.value = "teacher";
    }

    console.log("Utilisateur sélectionné :", userType.value);
  });
});

// Empêcher l'envoi du formulaire pour test
form.addEventListener('submit', (e) => {
  e.preventDefault(); // Empêche l'envoi du formulaire
  console.log("Formulaire soumis avec userType:", userType.value);
});

// Vérification au clic sur le bouton de soumission
submitButton.addEventListener('click', (e) => {
  console.log("Bouton soumis avec userType:", userType.value);
});

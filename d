{% load static %}
<link rel="stylesheet" href="{% static 'accounts/css/login.css' %}" />
{% include "ecole/header.html" %}

<section id="contact" class="contact section mt-5">
  <div class="container" data-aos="fade-up" data-aos-delay="100">
    <div class="row gy-4">
      <div class="col-lg-6">
        <section id="hero" class="hero section dark-background">
          <img src="{% static 'ecole/assets/img/hero-bg.jpg' %}" alt="" data-aos="fade-in">
        </section><!-- /Hero Section -->
      </div>

      <div class="col-lg-6 container">
        <div class="form shadow p-4 rounded">
          <h3 class="text-center mb-4">Inscription</h3>
          <div class="tabs row mb-4">
            <button class="tab col-5 active mx-auto" id="student-tab">
              <span class="bi bi-mortarboard me-2"></span>Élève
            </button>
            <button class="tab col-5 mx-auto" id="parent-tab">
              <span class="bi bi-people me-2"></span>Parent
            </button>
          </div>
          {% comment %} debut formulaire  {% endcomment %}
          <form class="login" method="post" action="{% url 'accounts:register' %}">
            {% csrf_token %}
            <div class="forms-tabs">
              <!-- Student form -->
              <div class="student-form mx-4 row active">
                <div class="mb-3 text-center">
                  <h5>Créer votre compte élève</h5>
                </div>
                <!-- ... existing code ... -->
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Prénom" name="prenom" class="form-control" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Nom" name="nom" class="form-control" required />
                </div>

                <div class="mb-3 input-group">
                  <select name="niveau" id="" class="form-control" required>
                    <option value="none" selected disabled>Niveau scolaire</option>
                    {% for op in opt %}
                    <optgroup label="{{ op.libelle }}">
                      {% for niv in op.niveaux_set.all %}
                      <option value="{{ niv.id }}">{{ niv.libelle }}</option>
                      {% endfor %}
                    </optgroup>
                    {% endfor %}
                  </select>
                </div>
                <!-- ... existing code ... -->
                <div class="mb-3 input-group">
                  <select name="genre" id="" class="form-control" required>
                    <option value="none" selected disabled>Genre</option>
                    <option value="M">Masculin</option>
                    <option value="F">Féminin</option>
                  </select>
                </div>
                <div class="mb-3 input-group">
                  <input type="date" placeholder="Date de naissance" name="dateNaissance"
                    class="form-control" id="dateNaissance" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Lieu de naissance" name="lieuNaissance"
                    class="form-control" id="lieueNaissance" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Prénom du père" name="prenomPere"
                    class="form-control" />
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Prénom de la mère" name="prenomMere"
                    class="form-control" />
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Nom de famille de la mère" name="nomMere"
                    class="form-control" />
                </div>
                <div class="mb-3 input-group">
                  <input type="email" placeholder="Email" name="email" class="form-control" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="password" name="password" id="std-password"
                    placeholder="Mot de passe" class="form-control" required>
                </div>
                <div class="mb-3 input-group">
                  <input type="password" name="passwordConfirmation" id="std-confirmPassword" 
                    placeholder="Confirmer le mot de passe" class="form-control" required>
                </div>
              </div>
              {% comment %} end ./student form {% endcomment %}

              <!-- Parent form -->
              <div class="parent-form mx-4 row hidden">
                <div class="mb-3 text-center">
                  <h5>Créer votre compte parent</h5>
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Prénom" name="p_prenom" class="form-control" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Nom" name="p_nom" class="form-control" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="text" placeholder="Adresse" name="p_adresse" class="form-control" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="email" placeholder="Email" name="p_email" class="form-control" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="tel" placeholder="Téléphone" name="p_telephone" class="form-control" required />
                </div>
                <div class="mb-3 input-group">
                  <input type="password" name="p_password" id="prt-password"
                    placeholder="Mot de passe" class="form-control" required>
                </div>
                <div class="mb-3 input-group">
                  <input type="password" name="p_passwordConfirmation" id="prt-confirmPassword" 
                    placeholder="Confirmer le mot de passe" class="form-control" required>
                </div>
              </div>{% comment %} fin formulaire parent {% endcomment %}
            </div>
            
            <div class="redirections text-center mt-3">
              <p>Déjà inscrit(e) ? <a href="{% url 'accounts:login' %}" class="text-primary">Se connecter</a></p>
              <p>Mot de passe oublié ? <a href="" class="text-primary">Réinitialiser</a></p>
            </div>
            <input type="text" name="user_type" id="user_type" value="student" hidden>

            <button type="submit" class="submit btn btn-primary w-100 mt-3">
              <span class="bi bi-person-plus me-2"></span>
              S'inscrire
            </button>
          </form>
        </div>
      </div>
      <!-- End Contact Form -->
    </div>
  </div>
</section>
<!-- /Contact Section -->

<script src="{% static 'accounts/js/form.js' %}"></script>

{% include "ecole/footer.html" %}
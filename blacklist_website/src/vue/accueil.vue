<template>
    <h3> Hi, welcome to the blacklist</h3>
    <p class="muted">Ready to blacklist ?</p>

    <div class="lin_container">
        <div class="signup">
            <router-link to="signup" class="btn"> signup </router-link>
        </div>
        <br><br>
        <div class="login">
            <router-link to="login" class="btn"> login </router-link>
        </div>
        <br><br>
        <div class="institution_signup">
            <router-link to="institution_signup" class="btn"> Register your institution ? </router-link>
        </div><br><br>
        <div class="blacklist">
            <router-link to="blacklist" class="btn"> go to blacklist </router-link>
        </div>
    </div>
    <br><br><br><br>
    <hr>
    <h3> Main tasks to do before 05/10 : </h3>
    - accès a la blacklist pour les utilisateurs non-authentifés ___ok<br>
    - accès à la page 'insertion' (besoin d'etre authentifiés) ___ok<br>
    - insertion de blacklistés (besoin d'etre authentifiés) ___ok<br>
    - ne pas insérer un blacklisté si doublon <br>
    - poossibilité de modifier un blacklisté <br>
    - les modifs de password <br>
    - page de création de compte pour les insititutions notamment (en grande partie pour ca enft) pour créer/modifier le 1e mot de passe <br>
</template>
<%inherit file="/subpage.mako"/>
<h1>PædagogNet</h1>
<form action="${url_for("user_login")}" method="post">
    <fieldset>
        <legend>Pædagog log-ind</legend>
        <p>Forkert adgangskode eller brugernavn</p>
        <label for="email">Email:</label><br />
        <input type="text" id="email" value=${esc_attr(email)} name="email"/><br />
        <label for="password">Adgangskode:</label><br />
        <input id="password" type="password" name="password"/><br />
        
        <input type="submit" value="Log ind!"/>
    </fieldset>
    <p>
        I tvivl? Ring til <strong>54 75 54 54</strong>
    </p>
</form>

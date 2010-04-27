<%inherit file="/subpage.mako"/>
<%!
    def title(self):
        return "Administration login"
    def section(self):
        return "other"
%>
<h1>PædagogNet</h1>
<form action="${url_for("admin_login")}" method="post">
    <fieldset>
        <legend>Administrator log-ind</legend>
        <label for="username">Brugernavn:</label><br />
        <input type="text" id="username" name="username"/><br />
        <label for="password">Adgangskode:</label><br />
        <input id="password" type="password" name="password"/><br />
        
        <input type="submit" value="Log ind!"/>
    </fieldset>
</form>

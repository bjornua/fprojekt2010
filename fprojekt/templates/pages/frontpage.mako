<%inherit file="/main.mako"/>
<h1>Velkommen til PædagogNet</h1>
<form action="${url_for("user_login")}" method="post" id="pedagogue_login">
    <fieldset>
        <legend>Pædagog log-ind</legend>
        <label for="email">Email:</label><br />
        <input type="text" id="email" name="email"/><br />
        <label for="password">Adgangskode:</label><br />
        <input id="password" type="password" name="password"/><br />
        <input type="submit" value="Log ind!"/>
    </fieldset>
    <p>
        I tvivl? Ring til <strong>54 75 54 54</strong>
    </p>
</form>
<form action="${url_for("institution_login")}" method="post" id="institution_login" style="display:none;">
    <fieldset>
        <legend>Institutions log-ind</legend>
        <label for="inst_code">Institutionskode:</label><br />
        <input name="password" type="password"/><br/>
        <input type="submit" value="Log ind!"/>
    </fieldset>
    <p>
        I tvivl? Ring til <strong>54 75 54 54</strong>
    </p>
</form>
<a id="pedagogue_activate_form" href="javascript:void()" style="display:none;">Pædagog log-ind</a>
<a id="institution_activate_form" href="javascript:void()">Log ind som institution</a>
<!--
<form action="${url_for("admin_login")}" method="post" id="adminstrator_login" style="display:none;">
    <fieldset>
        <legend>Administrator log-ind</legend>
        <label for="username">Brugernavn:</label><br />
        <input type="text" id="username" name="username"/><br />
        <label for="password">Adgangskode:</label><br />
        <input type="password" id="password" name="password"/><br />
        <input type="submit" value="Log ind!"/>
    </fieldset>
</form>
-->
<script type="text/javascript">
$(document).ready(function($){
    $("#pedagogue_activate_form").click(function () {
        $("#pedagogue_activate_form").css("display","none");
        $("#institution_activate_form").show("slow");
        $("#pedagogue_login").show("slow");
        $("#institution_login").hide("fast");
    })
    $("#institution_activate_form").click(function () {
        $("#institution_activate_form").css("display","none");
        $("#pedagogue_activate_form").show("slow");
        $("#institution_login").show("slow");
        $("#pedagogue_login").hide("fast");
    })
});
</script>

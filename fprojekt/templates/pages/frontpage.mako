<%inherit file="/subpage.mako"/>
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
</form>
<form action="${url_for("institution_login")}" method="post" id="institution_login">
    <fieldset>
        <legend>Institutions log-ind</legend>
        <label for="inst_code">Institutionskode:</label><br />
        <input name="password" type="password"/><br/>
        <input type="submit" value="Log ind!"/>
    </fieldset>
</form>
<p>
    I tvivl? Ring til <strong>54 75 54 54</strong>
</p>
<a id="pedagogue_activate_form" href="javascript:void()">Skift til pædagog log-ind</a>
<a id="institution_activate_form" href="javascript:void()">Skift til institution log-ind</a>
<script type="text/javascript">
$(document).ready(function($){
    $("#pedagogue_activate_form").click(function () {
        $("#pedagogue_activate_form").css("display","none");
        $("#institution_activate_form").css("display","block");
        $("#pedagogue_login").show("slow");
        $("#institution_login").hide("fast");
    })
    $("#institution_activate_form").click(function () {
        $("#institution_activate_form").css("display","none");
        $("#pedagogue_activate_form").css("display","block");
        $("#institution_login").show("slow");
        $("#pedagogue_login").hide("fast");
    })
});
</script>

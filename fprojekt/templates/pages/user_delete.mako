<%inherit file="/subpage.mako"/>
<%!
    def title(self):
        return u"Bekræft sletning"
    def section(self):
        return "other"
%>
<h1>Bekræftelse af sletning</h1>
<form action="${url_for("user_delete",id=id)}" method="post">
    <p>Er du sikker på at du vil slette denne bruger?</p>
    <table>
        <tr>
            <th><label for="sure_yes">Ja</label></th>
            <td><input type="radio" name="sure" id="sure_yes" value="yes"></td>
        </tr>
        <tr>
            <th><label for="sure_no">Nej</label></th>
            <td><input type="radio" name="sure" id="sure_no" value="no" checked="checked"></td>
        </tr>
        <tr>
            <th>&nbsp;</th>
            <td><input type="submit" value="Videre"></td>
        </tr>
    </table>
</form>

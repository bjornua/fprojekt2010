<%inherit file="/subpage.mako"/>
<%!
    def title(kwargs):
        return kwargs["name"]
    def section(kwargs):
        return "other"
%>
<h1>Bruger: ${escape(db_name)} &lt;${escape(db_email)}&gt;</h1>
<p>
    <a href="${url_for("user_delete",id=id)}">
        Slet
    </a>
</p>
<p>
    <a href="${url_for("institution_modify", id=inst_id)}">
        Tilbage til brugerliste
    </a>
</p>
<form action="${url_for("user_modify",id=id)}" method="post">
    <label for="id">Nr.:</label><br/>
    <input id="id" type="text" value="${id}" disabled="disabled"/><br/>
    
    <label for="name">Navn:</label><br/>
    <input type="text" id="name" value=${esc_attr(name)} name="name"/><br/>
    
    <label for="email">Email:</label><br/>
    <input type="text" id="email" value=${esc_attr(email)} name="email"/><br/>
    
    <label for="phone">Password:</label><br/>
    <input type="text" id="password" value=${esc_attr(password)} name="password"/><br/>
    
    <input type="submit" value="Gem ændringer"/>
    
    </table>
</form>

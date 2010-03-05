<%inherit file="/main_admin.mako"/>
<h1>Institution: ${escape(db_name)} (${escape(db_email)})</h1>
<p>
    <a href="${url_for("institution_delete",id=id)}">Slet</a>
</p>
<form action="${url_for("institution_modify",id=id)}" method="post">
    <label for="id">Nr.:</label><br/>
    <input id="id" type="text" value="${id}" disabled="disabled"/><br/>
    
    <label for="name">Navn:</label><br/>
    <input type="text" id="name" value=${esc_attr(name)} name="name"/><br/>
    
    <label for="email">Email:</label><br/>
    <input type="text" id="email" value=${esc_attr(email)} name="email"/><br/>
    
    <label for="phone">Telefon:</label><br/>
    <input type="text" id="phone" value=${esc_attr(phone)} name="phone"/><br/>

    <label for="phone">Password:</label><br/>
    <input type="text" id="password" value=${esc_attr(password)} name="password"/><br/>
    
    <input type="submit" value="Gem ændringer"/>
    
    </table>
</form>

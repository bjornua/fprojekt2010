<%inherit file="/main_editor.mako"/>
<%
initial_doc = {
    "title": document_title,
    "author": user_name,
    "sections": [{"id":x[0],"title":x[1],"content":x[2]} for x in document_sections]
}
%>




<form id="editor_area">
    <h1><span id="title_field"></span></h1>
    <h3>Skrevet af <span id="author_field"></span></h3>
</form>
<script type="text/javascript">
var doc = ${json(initial_doc)};



$("#author_field").text(doc.author);
$("#title_field").text(doc.title);

for(i in doc.sections){
    section = doc.sections[i];
    section.elements = {
        "container": document.createElement("div"),
        "title": document.createElement("h3"),
        "editor": document.createElement("textarea")
    };
    container = section.elements.container;
    title = section.elements.title;
    editor = section.elements.editor;

    $(container).append(title);    
    $(container).append(editor);    
    
    $(title).text(section.title);
    $(editor).text(section.content);
    
    $(editor).attr("id", "section" + String(section.id));

    $(container).addClass("section_container");
    $(title).addClass("section_title");
    $(editor).addClass("widgEditor");
    

    $("#editor_area").append(container);

}

</script>


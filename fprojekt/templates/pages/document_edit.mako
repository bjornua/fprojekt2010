<%inherit file="/main.mako"/>
<h1><span id="header" style="background:#CCC;">${escape(document_title)}</span></h1>
<p>Skrevet af <span style="background:#CCC;">${escape(user_name)}</span></p>
% for id, title, content in document_sections:
    <h3><span style="background:#CCC;">${escape(title)}</span></h3>
    <div style="background:#CCC;">${content}</div>
% endfor

<script type="text/javascript">
$("#header").click(function() {
    content = $(this).html()
    $(this).parent().html("<input type=\"text\" name=\"header\"/\>")
    $("#header").attr("value", content) 
})
</script>

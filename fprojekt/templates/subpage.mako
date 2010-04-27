<%inherit file="/xhtml11.mako"/>
<%
    title = self.attr.title(context.kwargs)
    section = self.attr.section(context.kwargs)
%>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>${escape(title)} - PædagogNet</title>
    <script type="text/javascript" src="/static/javascript/contrib/jquery-1.4.2.min.js"></script>
    <link media="screen" rel="stylesheet" type="text/css" href="/static/css/subpage/screen.css"/>
</head>
<div id="main" class=${esc_attr("section-"+section)}>
${widget.topmenu(section)}
${next.body()}
</div>

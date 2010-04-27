<%inherit file="/xhtml11.mako"/>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>${self.attr.title(context.kwargs)} - PædagogNet</title>
    <script type="text/javascript" src="/static/javascript/contrib/jquery-1.4.2.min.js"></script>
    <link media="screen" rel="stylesheet" type="text/css" href="/static/css/subpage/screen.css"/>
</head>
<div id="main" class=${esc_attr("section-" + self.attr.section(context.kwargs))}>
${widget.topmenu()}
${next.body()}
</div>

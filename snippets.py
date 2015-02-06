import os

current_path = os.path.dirname(os.path.abspath(__file__))
header = False
sub_header = False
footer = False
buttons = False
lists = False
cards = False
forms = False
toogle = False
checkbox = False
radio_button = False
range_control = False
select_control = False
tabs = False
actionSheet = False
backdrop = False
scrollDelegate = True


def create_snippet_string(tabTrigger, content, scope, description):
    tabTrigger_tag = "<tabTrigger>" + tabTrigger + "</tabTrigger>"
    content_tag = "<content><![CDATA[" + content + "]]></content>"
    scope_tag = "<scope>" + scope + "</scope>"
    if len(description) == 0:
        description_tag = "<description>...</description>"
    else:
        description_tag = "<description>" + description + "</description>"
    snippet_string = "<snippet>\n\t" + content_tag + "\n\t" + tabTrigger_tag +\
        "\n\t" + scope_tag + "\n\t" + description_tag + "\n" + "</snippet>"
    return snippet_string


def create_snippet_file(path_name_file, tabTrigger, content, scope, description):

	snippet_str = create_snippet_string(tabTrigger, content, scope, description)
	output_file = open(path_name_file, "w+")
	output_file.write(snippet_str)
	output_file.close()

if header:
    output_folder = current_path + '/Header/'
    css_bars = ['bar-light', 'bar-stable', 'bar-positive',
                'bar-calm', 'bar-balanced', 'bar-energized',
                            'bar-assertive', 'bar-royal', 'bar-dark']

    for bar in css_bars:
        header_str = '<div class="bar bar-header ' + bar + '"> \n' + \
            '\t <h1 class="title">${1:' + bar + '}</h1> \n' + '</div>'
        snippet_str = create_snippet_string(
            'ionic-header-' + bar[4:], header_str, 'text.html', 'ionic-header-' + bar[4:])
        print snippet_str
        print '----------'
        output_file = open(
            output_folder + 'ionic-header-' + bar[4:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

if sub_header:
    output_folder = current_path + '/SubHeader/'
    css_bars = ['bar-subheader']

    for bar in css_bars:
        strr = '<div class="bar ' + bar + '"> \n' + \
            '\t <h2 class="title">${1:' + bar + '}</h2> \n' + '</div>'
        snippet_str = create_snippet_string(
            'ionic-subheader', strr, 'text.html', bar + ' snippet')
        print snippet_str
        print '----------'
        output_file = open(
            output_folder + 'ionic-subheader' + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()


if footer:
    output_folder = current_path + '/Footer/'
    css_bars = ['bar-light', 'bar-stable', 'bar-positive',
                'bar-calm', 'bar-balanced', 'bar-energized',
                            'bar-assertive', 'bar-royal', 'bar-dark']

    for bar in css_bars:
        strr = '<div class="bar bar-footer ' + bar + '"> \n' + \
            '\t <div class="title">${1:' + bar + '}</div> \n' + '</div>'
        snippet_str = create_snippet_string(
            'ionic-footer-' + bar[4:], strr, 'text.html', 'ionic-footer-' + bar[4:])
        print snippet_str
        print '----------'
        output_file = open(
            output_folder + 'ionic-footer-' + bar[4:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()


if buttons:
    output_folder = current_path + '/Buttons/'
    css_buttons = ['button-light', 'button-stable', 'button-positive', 'button-calm',
                                                    'button-balanced', 'button-energized', 'button-assertive', 'button-royal', 'button-dark']

    for button_color in css_buttons:
        regular_button = '<button class="button ' + button_color + \
            '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
        block_button = '<button class="button button-block ' + button_color + \
            '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
        full_button = '<button class="button button-full ' + button_color + \
            '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
        small_button = '<button class="button button-small ' + button_color + \
            '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
        large_button = '<button class="button button-large ' + button_color + \
            '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
        outline_button = '<button class="button button-outline ' + \
            button_color + '"> \n' + \
            '\t ${1:' + button_color + '}\n' + '</button>'
        clear_button = '<button class="button button-clear ' + button_color + \
            '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
        icon_left_button = '<button class="button icon-left ${1:ionicon} ' + \
            button_color + '"> \n' + \
            '\t ${2:' + button_color + '}\n' + '</button>'
        icon_right_button = '<button class="button icon-right ${1:ionicon} ' + \
            button_color + '"> \n' + \
            '\t ${2:' + button_color + '}\n' + '</button>'
        button_bar = '<div class="button-bar bar-' + \
            button_color[7:] + '">$0</div>'

        snippet_str = create_snippet_string(
            'ionic-button-' + button_color[7:], regular_button, 'text.html', 'ionic-button-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string('ionic-button-block-' + button_color[
                                            7:], block_button, 'text.html', 'ionic-button-block-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-block-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string(
            'ionic-button-full-' + button_color[7:], full_button, 'text.html', 'ionic-button-full-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-full-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string('ionic-button-small-' + button_color[
                                            7:], small_button, 'text.html', 'ionic-button-small-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-small-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string('ionic-button-large-' + button_color[
                                            7:], large_button, 'text.html', 'ionic-button-large-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-large-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string('ionic-button-outline-' + button_color[
                                            7:], outline_button, 'text.html', 'ionic-button-outline-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-outline-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string('ionic-button-clear-' + button_color[
                                            7:], clear_button, 'text.html', 'ionic-button-clear-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-clear-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string('ionic-button-icon-left-' + button_color[
                                            7:], icon_left_button, 'text.html', 'ionic-button-icon-left-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-icon-left-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string('ionic-button-icon-right-' + button_color[
                                            7:], icon_right_button, 'text.html', 'ionic-button-icon-right-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-icon-right-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        snippet_str = create_snippet_string(
            'ionic-button-bar-' + button_color[7:], button_bar, 'text.html', 'ionic-button-bar-' + button_color[7:])
        output_file = open(
            output_folder + 'ionic-button-bar-' + button_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

if lists:

    output_folder = current_path + '/Lists/'
    item_divider = '<div class="item item-divider">$0</div>'
    item_icon_left = '<a class="item item-icon-left" href="#">$0</a>'
    item_icon_right = '<a class="item item-icon-right" href="#">$0</a>'
    item_icon_left_right = '<a class="item item-icon-left item-icon-right" href="#">$0</a>'
    item_button_right = '<a class="item item-button-right" href="#">$0</a>'
    item_button_left = '<a class="item item-button-left" href="#">$0</a>'
    item_avatar = '<a class="item item-avatar" href="#">\n' + \
        '\t<img src="${1:image_source}">\n' + \
        '\t<h2>${2:title}</h2>\n' + '\t<p>${3:description}</p>\n' + '</a>'
    item_thumbnail_left = '<a class="item item-thumbnail-left" href="#">\n' + \
        '\t<img src="${1:image_source}">\n' + \
        '\t<h2>${2:title}</h2>\n' + '\t<p>${3:description}</p>\n' + '</a>'
    item_thumbnail_right = '<a class="item item-thumbnail-right" href="#">\n' + \
        '\t<img src="${1:image_source}">\n' + \
        '\t<h2>${2:title}</h2>\n' + '\t<p>${3:description}</p>\n' + '</a>'
    list_inset = '<div class="list list-inset">$0</div>'
    collection_repeat = '<div class="item ${1:your_item_css_class}"\n' + '\tcollection-repeat="${2:item in items}"\n' + '\tcollection-item-width="${3:\'100%\'}"\n' + \
        '\tcollection-item-height="${4:getItemHeight(item, \$index)}"\n' + \
        '\tng-style="${5:{height: getItemHeight(item, \$index)}\}">$0\n' + \
        '</div>'

    ionicListDelegate_showReorder = '\$ionicListDelegate.showReorder(${1:true});'
    ionicListDelegate_showDelete = '\$ionicListDelegate.showDelete(${1:true});'
    ionicListDelegate_canSwipeItems = '\$ionicListDelegate.canSwipeItems(${1:true});'
    ionicListDelegate_closeOptionButtons = '\$ionicListDelegate.closeOptionButtons();'

    snippet_str = create_snippet_string(
        'ionic-item-divider', item_divider, 'text.html', 'ionic-item-divider')
    output_file = open(
        output_folder + 'ionic-item-divider' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-icon-left', item_icon_left, 'text.html', 'ionic-item-icon-left')
    output_file = open(
        output_folder + 'ionic-item-icon-left' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-icon-right', item_icon_right, 'text.html', 'ionic-item-icon-right')
    output_file = open(
        output_folder + 'ionic-item-icon-right' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-icon-left-right', item_icon_left_right, 'text.html', 'ionic-item-icon-left-right')
    output_file = open(
        output_folder + 'ionic-item-icon-left-right' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-button-right', item_button_right, 'text.html', 'ionic-item-button-right')
    output_file = open(
        output_folder + 'ionic-item-button-right' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-button-left', item_button_left, 'text.html', 'ionic-item-button-left')
    output_file = open(
        output_folder + 'ionic-item-button-left' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-avatar', item_avatar, 'text.html', 'ionic-item-avatar')
    output_file = open(
        output_folder + 'ionic-item-avatar' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-thumbnail-left', item_thumbnail_left, 'text.html', 'ionic-item-thumbnail-left')
    output_file = open(
        output_folder + 'ionic-item-thumbnail-left' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-item-thumbnail-right', item_thumbnail_right, 'text.html', 'ionic-item-thumbnail-right')
    output_file = open(
        output_folder + 'ionic-item-thumbnail-right' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-list-inset', list_inset, 'text.html', 'ionic-list-inset')
    output_file = open(
        output_folder + 'ionic-list-inset' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-collection-repeat', collection_repeat, 'text.html', 'ionic-collection-repeat')
    output_file = open(
        output_folder + 'ionic-collection-repeat' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        '$ionicListDelegate.showReorder', ionicListDelegate_showReorder, 'source.js', 'Ionic List Delegate')
    output_file = open(
        output_folder + 'ionicListDelegate.showReorder' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        '$ionicListDelegate.showDelete', ionicListDelegate_showDelete, 'source.js', 'Ionic List Delegate')
    output_file = open(
        output_folder + 'ionicListDelegate.showDelete' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        '$ionicListDelegate.canSwipeItems', ionicListDelegate_canSwipeItems, 'source.js', 'Ionic List Delegate')
    output_file = open(
        output_folder + 'ionicListDelegate.canSwipeItems' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        '$ionicListDelegate.closeOptionButtons', ionicListDelegate_closeOptionButtons, 'source.js', 'Ionic List Delegate')
    output_file = open(
        output_folder + 'ionicListDelegate.closeOptionButtons' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

if cards:

    output_folder = current_path + '/Cards/'
    card = '<div class="card">\n' + '\t<div class="item item-text-wrap">\n' + \
        '\t\t${1:desc}\n' + '\t</div>\n' + '</div>'
    card_header = '<div class="card">\n' + '\t<div class="item item-divider">\n' + \
        '\t\t${1:header}\n' + '\t</div>\n' + '\t<div class="item item-text-wrap">\n' + \
        '\t\t${2:desc}\n' + '\t</div>\n' + '</div>'
    card_footer = '<div class="card">\n' + '\t<div class="item item-text-wrap">\n' + \
        '\t\t${1:desc}\n' + '\t</div>\n' + '\t<div class="item item-divider">\n' + \
        '\t\t${2:footer}\n' + '\t</div>\n' + '</div>'
    card_header_footer = '<div class="card">\n' + '\t<div class="item item-divider">\n' + \
        '\t\t${1:header}\n' + '\t</div>\n' + '\t<div class="item item-text-wrap">\n' + '\t\t${2:desc}\n' + \
        '\t</div>\n' + '\t<div class="item item-divider">\n' + \
        '\t\t${3:footer}\n' + '\t</div>\n' + '</div>'
    card_list_item = '<a href="#" class="item item-icon-left">\n' + \
        '\t<i class="icon ${1:ionicon}"></i>\n' + '\t${2:desc}\n' + '</a>'
    card_list = '<div class="list card">\n' + '\t$0\n' + '</div>'

    item_avatar = '<div class="item item-avatar" href="#">\n' + \
        '\t<img src="${1:image_source}">\n' + '\t<h2>${2:title}</h2>\n' + \
        '\t<p>${3:description}</p>\n' + '</div>\n'
    item_image = '<div class="item item-image">\n' + \
        '\t<img src="${4:image_source}">\n' + '</div>\n'
    item_link = '<a class="item ${5:item-icon-left} ${6:assertive}" href="#">\n' + \
        '\t<i class="icon ${7:ionicon}"></i>\n' + '\t${8:text_link}\n' + '</a>'
    card_image = item_avatar + item_image + item_link

    item_body = '<div class="item item-body">\n' + \
        '\t<img class="full-image" src="${4:image_source}">\n' + \
        '\t<p>${5:description}</p>\n' + \
        '\t<p>\n' + \
        '\t\t<a href="#" class="subdued">1 Like</a>\n' + \
        '\t\t<a href="#" class="subdued">5 Comments</a>\n' + \
        '\t</p>\n' + \
        '</div>\n\n'

    item_tabs = '<div class="item tabs tabs-secondary tabs-icon-left">\n' + \
        '\t<a class="tab-item" href="#">\n' + \
        '\t\t<i class="icon ion-thumbsup"></i>\n' + \
        '\t\tLike\n' + \
        '\t</a>\n' + \
        '\t<a class="tab-item" href="#">\n' + \
        '\t\t<i class="icon ion-chatbox"></i>\n' + \
        '\t\tComments\n' + \
        '\t</a>\n' + \
        '\t<a class="tab-item" href="#">\n' + \
        '\t\t<i class="icon ion-share"></i>\n' + \
        '\t\tShare\n' + \
        '\t</a>\n' + \
        '</div>\n'

    card_showcase = item_avatar + item_body + item_tabs

    snippet_str = create_snippet_string(
        'ionic-card', card, 'text.html', 'ionic-card')
    output_file = open(output_folder + 'ionic-card' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-card-header', card_header, 'text.html', 'ionic-card-header')
    output_file = open(
        output_folder + 'ionic-card-header' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-card-footer', card_footer, 'text.html', 'ionic-card-footer')
    output_file = open(
        output_folder + 'ionic-card-footer' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-card-header-footer', card_header_footer, 'text.html', 'ionic-card-header-footer')
    output_file = open(
        output_folder + 'ionic-card-header-footer' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-card-list-item', card_list_item, 'text.html', 'ionic-card-list-item')
    output_file = open(
        output_folder + 'ionic-card-list-item' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-card-list', card_list, 'text.html', 'ionic-card-list')
    output_file = open(
        output_folder + 'ionic-card-list' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-card-image', card_image, 'text.html', 'ionic-card-image')
    output_file = open(
        output_folder + 'ionic-card-image' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-card-showcase', card_showcase, 'text.html', 'ionic-card-showcase')
    output_file = open(
        output_folder + 'ionic-card-showcase' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

if forms:
    output_folder = current_path + '/Forms/'

    basic_input_html_start = '<label class="item item-input'
    basic_input_html_end = '</label>'
    input_placeholder = basic_input_html_start + '">\n' + \
        '\t<input type="text" placeholder="${1:placeholder_1}">\n' + \
        basic_input_html_end

    input_inline = basic_input_html_start + '">\n' + \
        '\t<span class="input-label">${1:input_name}</span>\n' + \
        '\t<input type="text">\n' + \
        basic_input_html_end

    input_stacked = basic_input_html_start + ' item-stacked-label">\n' + \
        '\t<span class="input-label">${1:input_name}</span>\n' + \
        '\t<input type="text" placeholder="${2:input_placeholder}">\n' + \
        basic_input_html_end

    input_floating = basic_input_html_start + ' item-floating-label">\n' + \
        '\t<span class="input-label">${1:input_name}</span>\n' + \
        '\t<input type="text" placeholder="${2:input_placeholder}">\n' + \
        basic_input_html_end

    input_inset = '<div class="item item-input-inset">\n' + \
        '\t<label class="item-input-wrapper">\n' + \
        '\t\t<input type="text" placeholder="${1:input_placeholder}">\n' + \
        '\t</label>\n' + \
        '\t<button class="button button-small">\n' + \
        '\t\t${2:button_name}\n' + \
        '\t</button>\n' + \
        '</div>\n'

    input_icon = basic_input_html_start + '">\n' + \
        '\t<i class="icon ion-search placeholder-icon"></i>\n' + \
        '\t<input type="text" placeholder="${1:Search}">\n' + \
        basic_input_html_end

    input_header = '<div class="bar bar-header item-input-inset">\n' + \
        '\t<label class="item-input-wrapper">\n' + \
        '\t\t<i class="icon ion-ios7-search placeholder-icon"></i>\n' + \
        '\t\t<input type="search" placeholder="${1:Search}">\n' + \
        '\t</label>\n' + \
        '\t<button class="button button-clear">\n' + \
        '\t\t${2:Cancel}\n' + \
        '\t</button>\n' + \
        '</div>'

    snippet_str = create_snippet_string(
        'ionic-input-placeholder', input_placeholder, 'text.html', 'ionic-input-placeholder')
    output_file = open(
        output_folder + 'ionic-input-placeholder' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-input-inline', input_inline, 'text.html', 'ionic-input-inline')
    output_file = open(
        output_folder + 'ionic-input-inline' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-input-stacked', input_stacked, 'text.html', 'ionic-input-stacked')
    output_file = open(
        output_folder + 'ionic-input-stacked' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-input-floating', input_floating, 'text.html', 'ionic-input-floating')
    output_file = open(
        output_folder + 'ionic-input-floating' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-input-inset', input_inset, 'text.html', 'ionic-input-inset')
    output_file = open(
        output_folder + 'ionic-input-inset' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-input-icon', input_icon, 'text.html', 'ionic-input-icon')
    output_file = open(
        output_folder + 'ionic-input-icon' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

    snippet_str = create_snippet_string(
        'ionic-input-header', input_header, 'text.html', 'ionic-input-header')
    output_file = open(
        output_folder + 'ionic-input-header' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

if toogle:
    output_folder = current_path + '/Toggle/'

    css_toggles = ['toggle-light', 'toggle-stable', 'toggle-positive',
                   'toggle-calm', 'toggle-balanced', 'toggle-energized',
                   'toggle-assertive', 'toggle-royal', 'toggle-dark']

    for toggle_color in css_toggles:
        toggle_str = '<li class="item item-toggle">\n' + \
            '\t${1:desc}\n' + \
            '\t<label class="toggle ' + toggle_color + '">\n' + \
            '\t\t<input type="checkbox">\n' + \
            '\t\t<div class="track">\n' + \
            '\t\t\t<div class="handle"></div>\n' + \
            '\t\t</div>\n' + \
            '\t</label>\n' + \
            '</li>\n'

        snippet_str = create_snippet_string('ionic-toggle-' + toggle_color[7:], toggle_str,
                                            'text.html', 'ionic-toggle-' + toggle_color[7:])
        output_file = open(
            output_folder + 'ionic-toggle-' + toggle_color[7:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

if checkbox:
    output_folder = current_path + '/Checkbox/'

    css_checkboxs = ['checkbox-light', 'checkbox-stable', 'checkbox-positive',
                     'checkbox-calm', 'checkbox-balanced', 'checkbox-energized',
                     'checkbox-assertive', 'checkbox-royal', 'checkbox-dark']

    for checkbox_color in css_checkboxs:
        checkbox_str = '<li class="item item-checkbox">\n' + \
            '\t<label class="checkbox ' + checkbox_color + '">\n' + \
            '\t\t<input type="checkbox">\n' + \
            '\t</label>\n' + \
            '\t${1:desc}\n' + \
            '</li>\n'

        snippet_str = create_snippet_string('ionic-checkbox-' + checkbox_color[9:], checkbox_str,
                                            'text.html', 'ionic-checkbox-' + checkbox_color[9:])
        output_file = open(
            output_folder + 'ionic-checkbox-' + checkbox_color[9:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

if radio_button:
    output_folder = current_path + '/Radio Buttons/'

    radio_str = '<label class="item item-radio">\n' + \
                '\t<input type="radio" name="group">\n' + \
                '\t<div class="item-content">\n' + \
                '\t\t${1:desc}\n' + \
                '\t</div>\n' + \
                '\t<i class="radio-icon ${2:ion-checkmark}"></i>\n' + \
                '</label>\n'

    snippet_str = create_snippet_string(
        'ionic-radio-button', radio_str, 'text.html', 'ionic-radio-button')
    output_file = open(
        output_folder + 'ionic-radio-button.sublime-snippet', 'w+')
    output_file.write(snippet_str)
    output_file.close()

if range_control:

    output_folder = current_path + '/Range/'

    css_ranges = ['range-light', 'range-stable', 'range-positive',
                  'range-calm', 'range-balanced', 'range-energized',
                  'range-assertive', 'range-royal', 'range-dark']

    for range_color in css_ranges:
        range_str_default = '<div class="range ' + range_color + '">\n' + \
            '\t<i class="icon ${1:ion-volume-low}"></i>\n' + \
            '\t<input type="range" name="volume" min="0" max="100" value="33">\n' + \
            '\t<i class="icon ${2:ion-volume-high}"></i>\n' + \
            '</div>\n'

        snippet_str = create_snippet_string('ionic-range-' + range_color[6:], range_str_default,
                                            'text.html', 'ionic-range-' + range_color[6:])
        output_file = open(
            output_folder + 'ionic-range-' + range_color[6:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        range_str_in_list = '<div class="item range ' + range_color + '">\n' + \
            '\t<i class="icon ${1:ion-volume-low}"></i>\n' + \
            '\t<input type="range" name="volume" min="0" max="100" value="33">\n' + \
            '\t<i class="icon ${2:ion-volume-high}"></i>\n' + \
            '</div>\n'

        snippet_str = create_snippet_string('ionic-range-item-' + range_color[6:], range_str_in_list,
                                            'text.html', 'ionic-range-item-' + range_color[6:])
        output_file = open(
            output_folder + 'ionic-range-item-' + range_color[6:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

if select_control:
    output_folder = current_path + '/Select/'

    css_selects = ['item-light', 'item-stable', 'item-positive',
                   'item-calm', 'item-balanced', 'item-energized',
                   'item-assertive', 'item-royal', 'item-dark']

    for select_color in css_selects:
        select_str = '<label class="item item-input item-select ' + select_color + '">\n' + \
            '\t<div class="input-label">\n' + \
            '\t\t${1:desc}\n' + \
            '\t</div>\n' + \
            '\t<select>\n' + \
            '\t\t<option selected>${2:opt1}</option>\n' + \
            '\t\t<option>${3:opt2}</option>\n' + \
            '\t<select>\n' + \
            '</label>\n'

        snippet_str = create_snippet_string('ionic-select-' + select_color[5:], select_str,
                                            'text.html', 'ionic-select-' + select_color[5:])
        output_file = open(
            output_folder + 'ionic-select-' + select_color[5:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

if tabs:
    output_folder = current_path + '/Tabs/'

    css_tabs = ['tabs-light', 'tabs-stable', 'tabs-positive',
                'tabs-calm', 'tabs-balanced', 'tabs-energized',
                'tabs-assertive', 'tabs-royal', 'tabs-dark']

    for tabs_color in css_tabs:
        tabs_str_default = '<div class="tabs ' + tabs_color + '">\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t${1:Tab1}\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t${2:Tab2}\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t${3:Tab3}\n' + \
            '\t</a>\n' + \
            '</div>\n'

        snippet_str = create_snippet_string('ionic-tabs-' + tabs_color[5:], tabs_str_default,
                                            'text.html', 'ionic-tabs-' + tabs_color[5:])
        output_file = open(
            output_folder + 'ionic-tabs-' + tabs_color[5:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        tabs_str_icon_only = '<div class="tabs tabs-icon-only ' + tabs_color + '">\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${1:ion-home}"></i>\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${2:ion-star}"></i>\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${3:ion-gear-a}"></i>\n' + \
            '\t</a>\n' + \
            '</div>\n'

        snippet_str = create_snippet_string('ionic-tabs-icon-only-' + tabs_color[5:], tabs_str_icon_only,
                                            'text.html', 'tabs-icon-only-' + tabs_color[5:])
        output_file = open(
            output_folder + 'ionic-tabs-icon-only-' + tabs_color[5:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        tabs_str_icon_top = '<div class="tabs tabs-icon-top ' + tabs_color + '">\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${1:ion-home}"></i>\n' + \
            '\t\t${2:Tab1}\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${3:ion-star}"></i>\n' + \
            '\t\t${4:Tab2}\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${5:ion-gear-a}"></i>\n' + \
            '\t\t${6:Tab3}\n' + \
            '\t</a>\n' + \
            '</div>\n'

        snippet_str = create_snippet_string('ionic-tabs-icon-top-' + tabs_color[5:], tabs_str_icon_top,
                                            'text.html', 'tabs-icon-top-' + tabs_color[5:])
        output_file = open(
            output_folder + 'ionic-tabs-icon-top-' + tabs_color[5:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        tabs_str_icon_left = '<div class="tabs tabs-icon-left ' + tabs_color + '">\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${1:ion-home}"></i>\n' + \
            '\t\t${2:Tab1}\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${3:ion-star}"></i>\n' + \
            '\t\t${4:Tab2}\n' + \
            '\t</a>\n' + \
            '\t<a class="tab-item" href="#">\n' + \
            '\t\t<i class="icon ${5:ion-gear-a}"></i>\n' + \
            '\t\t${6:Tab3}\n' + \
            '\t</a>\n' + \
            '</div>\n'

        snippet_str = create_snippet_string('ionic-tabs-icon-left-' + tabs_color[5:], tabs_str_icon_left,
                                            'text.html', 'tabs-icon-left-' + tabs_color[5:])
        output_file = open(
            output_folder + 'ionic-tabs-icon-left-' + tabs_color[5:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

        tabs_str_striped = '<div class="tabs-striped tabs-color-' + tabs_color[5:] + '">\n' + \
            '\t<div class="tabs">\n' + \
            '\t\t<a class="tab-item" href="#">\n' + \
            '\t\t\t<i class="icon ${1:ion-home}"></i>\n' + \
            '\t\t\t${2:Tab1}\n' + \
            '\t\t</a>\n' + \
            '\t\t<a class="tab-item" href="#">\n' + \
            '\t\t\t<i class="icon ${3:ion-star}"></i>\n' + \
            '\t\t\t${4:Tab2}\n' + \
            '\t\t</a>\n' + \
            '\t\t<a class="tab-item" href="#">\n' + \
            '\t\t\t<i class="icon ${5:ion-gear-a}"></i>\n' + \
            '\t\t\t${6:Tab3}\n' + \
            '\t\t</a>\n' + \
            '\t</div>\n' + \
            '</div>\n'

        snippet_str = create_snippet_string('ionic-tabs-striped-' + tabs_color[5:], tabs_str_striped,
                                            'text.html', 'tabs-striped-' + tabs_color[5:])
        output_file = open(
            output_folder + 'ionic-tabs-striped-' + tabs_color[5:] + ".sublime-snippet", "w+")
        output_file.write(snippet_str)
        output_file.close()

if actionSheet:
    output_folder = current_path + '/Action Sheet/'
    actionSheet_str = '\$ionicActionSheet.show({\n' + \
        '\t\tbuttons: [\n' + \
        '\t\t\t{ text: "${1:Button text 1}" },\n' + \
        '\t\t\t{ text: "${2:Move}" }\n' + \
        '\t\t],\n' + \
        '\t\tdestructiveText: "${3:Delete}",\n' + \
        '\t\ttitleText: "${4:Title}",\n' + \
        '\t\tcancelText: "${5:Cancel}",\n' + \
        '\t\tcancel: function() {\n' + \
        '\t\t\t${6: //your code goes here}\n' + \
        '\t\t},\n' + \
        '\t\tbuttonClicked: function(index) {\n' + \
        '\t\t\t${7: return true;}\n' + \
        '\t\t}\n' + \
        '});'

    snippet_str = create_snippet_string(
        '$ionicActionSheet.show', actionSheet_str, 'source.js', 'Ionic Action Sheet')
    output_file = open(
        output_folder + 'ionicActionSheet.show' + ".sublime-snippet", "w+")
    output_file.write(snippet_str)
    output_file.close()

if backdrop:
	output_folder = current_path + '/Backdrop/'
	backdrop_retain = '\$ionicBackdrop.retain();'
	backdrop_release = '\$ionicBackdrop.release();'

	snippet_str = create_snippet_string(
            '$ionicBackdrop.retain', backdrop_retain, 'source.js', 'Ionic Backdrop')
	output_file = open(
            output_folder + 'ionicBackdrop.retain' + ".sublime-snippet", "w+")
	output_file.write(snippet_str)
	output_file.close()

   	snippet_str = create_snippet_string(
            '$ionicBackdrop.release', backdrop_release, 'source.js', 'Ionic Backdrop')
	output_file = open(
            output_folder + 'ionicBackdrop.release' + ".sublime-snippet", "w+")
	output_file.write(snippet_str)
	output_file.close()

if scrollDelegate:
	output_folder = current_path + '/Content/'
	service = '\$ionicScrollDelegate.'
	resize = service + 'resize()'
	scrollTop = service + 'scrollTop(${1:shouldAnimate})'
	scrollBottom = service + 'scrollBottom(${1:shouldAnimate})'
	scrollTo = service + 'scrollTo(${1:left}, ${2:top}, ${3:shouldAnimate})'
	scrollBy = service + 'scrollBy(${1:left}, ${2:top}, ${3:shouldAnimate})'
	zoomTo = service + 'zoomTo(${1:level}, ${2:animate}, ${3:originLeft}, ${4:originTop})'
	zoomBy = service + 'zoomBy(${1:factor}, ${2:animate}, ${3:originLeft}, ${4:originTop})'
	getScrollPosition = service + 'getScrollPosition()'
	anchorScroll = service + 'anchorScroll(${1:shouldAnimate})'
	getScrollView = service + 'getScrollView()'
	getByHandle = service + '\$getByHandle(${1:handle})'

	path_name_file = output_folder + 'ionicScrollDelegate.resize' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.resize'
	content = resize
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.scrollTop' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.scrollTop'
	content = scrollTop
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.scrollBottom' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.scrollBottom'
	content = scrollBottom
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.scrollTo' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.scrollTo'
	content = scrollTo
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.scrollBy' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.scrollBy'
	content = scrollBy
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.zoomTo' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.zoomTo'
	content = zoomTo
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.zoomBy' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.zoomBy'
	content = zoomBy
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.getScrollPosition' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.getScrollPosition'
	content = getScrollPosition
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.anchorScroll' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.anchorScroll'
	content = anchorScroll
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.getScrollView' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.getScrollView'
	content = getScrollView
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

	path_name_file = output_folder + 'ionicScrollDelegate.getByHandle' + ".sublime-snippet"
	tabTrigger = '$ionicScrollDelegate.getByHandle'
	content = getByHandle
	scope = 'source.js'
	description = ' Ionic ScrollDelegate'
	create_snippet_file(path_name_file, tabTrigger, content, scope, description)

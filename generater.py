import toml


def read_toml(file_path):
    try:
        data = toml.load(file_path)
        return data
    except Exception as e:
        raise ImportError(f"Error reading file: {file_path}. {e}")


file_path = "bookmarks.toml"
bookmark_datas = read_toml(file_path)
# print(bookmark_datas)

tabs_nav_html = ""
"""
Example:
    <button type="button" class="snap-start hs-tab-active:font-semibold hs-tab-active:border-brown-600 hs-tab-active:text-brown-600 py-4 px-2 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-brown-600 focus:outline-hidden focus:text-brown-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-brown-500 active" id="tabs-centered-item-1" aria-selected="true" data-hs-tab="#tabs-centered-1" aria-controls="tabs-centered-1" role="tab">
        Tab 1
    </button>
    <button type="button" class="snap-start hs-tab-active:font-semibold hs-tab-active:border-brown-600 hs-tab-active:text-brown-600 py-4 px-2 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-brown-600 focus:outline-hidden focus:text-brown-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-brown-500" id="tabs-centered-item-2" aria-selected="false" data-hs-tab="#tabs-centered-2" aria-controls="tabs-centered-2" role="tab">
        Tab 2
    </button>
    <div class="md:pe-14 snap-start">
        <button type="button" class="snap-start hs-tab-active:font-semibold hs-tab-active:border-brown-600 hs-tab-active:text-brown-600 py-4 px-2 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-brown-600 focus:outline-hidden focus:text-brown-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-brown-500" id="tabs-centered-item-15" aria-selected="false" data-hs-tab="#tabs-centered-15" aria-controls="tabs-centered-15" role="tab">
        Tab 15
        </button>
    </div>
"""
index = 0
for tab_name in bookmark_datas.keys():
    if index == 0:
        tabs_nav_html += f"""
<button type="button" class="snap-start hs-tab-active:font-semibold hs-tab-active:border-brown-600 hs-tab-active:text-brown-600 py-4 px-2 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-brown-600 focus:outline-hidden focus:text-brown-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-brown-500 active" id="tabs-{tab_name}-item" aria-selected="true" data-hs-tab="#tabs-{tab_name}" aria-controls="tabs-{tab_name}" role="tab">
    {tab_name}
</button>
"""
    elif 0 < index < len(bookmark_datas.keys()) - 1:
        tabs_nav_html += f"""
<button type="button" class="snap-start hs-tab-active:font-semibold hs-tab-active:border-brown-600 hs-tab-active:text-brown-600 py-4 px-2 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-brown-600 focus:outline-hidden focus:text-brown-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-brown-500" id="tabs-{tab_name}-item" aria-selected="false" data-hs-tab="#tabs-{tab_name}" aria-controls="tabs-{tab_name}" role="tab">
    {tab_name}
</button>
"""
    elif index == len(bookmark_datas.keys()) - 1:
        tabs_nav_html += f"""
<div class="md:pe-14 snap-start">
    <button type="button" class="snap-start hs-tab-active:font-semibold hs-tab-active:border-brown-600 hs-tab-active:text-brown-600 py-4 px-2 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-brown-600 focus:outline-hidden focus:text-brown-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-brown-500" id="tabs-{tab_name}-item" aria-selected="false" data-hs-tab="#tabs-{tab_name}" aria-controls="tabs-{tab_name}" role="tab">
    {tab_name}
    </button>
</div>
"""
    index += 1


def get_bm_item_html(title: str, caption: str, url: str, icon: str):
    return f"""\
<a class="border-1 border-gray-200 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-200 dark:hover:bg-neutral-700 rounded-xl flex flex-col p-4 hover:shadow-lg"
    href="{url}">
    <div width="36px" height="36px" style="background-image: url('{icon}')" class="h-8 w-8 bg-contain bg-no-repeat bg-center rounded border-2 border-white bg-white"></div>
    <p class="font-bold pt-3 pb-0 m-0">{title}</p>
    <p class="p-0">{caption}</p>
</a>
"""


tabs_content_html = ""
index = 0
for tab_name, tab_contents in bookmark_datas.items():
    body_html = f"""<div id="tabs-{tab_name}" class="{"hidden" if index != 0 else ""}" role="tabpanel" aria-labelledby="tabs-{tab_name}-item">"""

    for group_title, bookmarks in tab_contents.items():
        body_html += f"""<h3 class="font-semibold text-2xl text-gray-800 dark:text-neutral-200 py-3">{group_title}</h3>"""
        body_html += f"""<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 2xl:grid-cols-6 gap-4 mb-12">"""
        for bookmark in bookmarks:
            body_html += get_bm_item_html(
                bookmark.get("title", ""),
                bookmark.get("caption", ""),
                bookmark.get("url", "#"),
                bookmark.get("icon", "/favicon.png"),
            )
        body_html += "</div>"
    body_html += "</div>"
    tabs_content_html += body_html
    index += 1

html_head = """\
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="module" crossorigin src="./static/preline.js"></script>
    <link rel="stylesheet" crossorigin href="./static/all.css">
</head>
"""

header_html = """\
<header class="relative flex flex-wrap sm:justify-start sm:flex-nowrap w-full bg-white text-sm py-3 dark:bg-neutral-800 drop-shadow-lg">
    <nav class="max-w-[85rem] w-full mx-auto px-4 sm:flex sm:items-center sm:justify-between">
    <div class="flex items-center justify-between">
        <a class="flex text-xl font-semibold dark:text-white focus:outline-hidden focus:opacity-80 items-center" href="#" aria-label="Brand">
        <span class="inline-flex items-center gap-x-3 text-xl font-semibold dark:text-white">
            <img class="w-10" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAv4SURBVHgB7Z1LbFTXGce/GT9mwDY2hBA3tGSSIqhEwEglWGpTcDa0m6SwqFpFqkJUddEqKmHRTReJyaKbLgpVVFWqIlxVqlplAUk2LVkEaFqpLlJwoQsoDYZgxzbGHr/iGXts5/wv9zpnvnvnPsaPuefc85OOr33mnhl7vv/3OOfeM07RKrC0tNQmDkdF6xAtJ9p+0drs5uK1n/2UDG7e+M1v/R7ut9tV0fpEu5hKpfpphdRTldhGPyFal90Ma0vObl1Oh7ABxHCGViCGyAKQDP8qVfBww7qBSHsW3wi79IjDqahCSEc5WbzI6+JwW7RuMsaPG8dFu23bKDShIoB40pw4nKOHivNkrlCgufl5misWaX5+jpYWF2lRNEN4Bj+569mfTqeprr6e6urqqaGhgTKZDDVms5WeplvY67g4PhcmGgQKQDzZS+Jwmjw8HgaemZqimekpY+w1BO/t4twcCfeiwizRlOiDICCE5k2tVF/vMmNOtI+E7V4WIjjv99y+KcAOJz3EjI9faGJ8nIYG7tHU5IQxfg1YKJXos5kZGvl0kPJjD6gkfmbAZueCUkLFCGAP7Ob901OTND05aYweIyCEoki9LSIabGxq4g8jJZCIBKe8xnpGADEAc/pu3g+vn8znjfFjCCICIsFkftzr4W47lbtwCcAu+M7KfTD46MiIlesN8WZa1GT3h4e8nPS0bdsyvCLAB8Ry/oP7I6K6L5BBDeZFwTg2Osq7rZqAd5YJwM77ObkPYR9PaFALOKxHOtgvbNwtdywLwA4PZQ+iuDBhX12QDjBNZ5ywV3Mt5AhQNl3AtAJTPIPaeEzTYfxXnR8sAdjef1w+a1oMXHDPLQ2KAeNPux15OQo4EaBLfrRkLzIY9ACpoFIUcARwomyACf3a4VELHMaXtB3+yy7yYFXJoBcexXwX0gAiQJfci+mDyf36gRRQLLjWco5CAOXeXzDeryslcbmesR8C6JB7cC3foCdF92puDgLIyT2l0gIZ9GTeHQE6XAJYNPlfW5bcF4jaXBeDFpfMpV5dWQwjAEOyMAJIOEYACccIIOEYASQcI4CEYwSQcIwAEo4RQMIxAkg4VX9ARBzIbNhAu5/eS+2Pb6dsdgPlx8fozv9vWc2PJ7660xqHMaAfYz6+RRNjY76vk3tqJ+3YuZPaNm+hwuwsDQ8OUN+/e+k/V3pJVZQUAAx46Mh3rKMXvX+/RBfeKd8DASN2fuswHRQtu2FD2WP7njlIeWH8t3vesowqjzksXmffgYOuMfgZr++ICWNVRCkBtG7ZQi98/8WKhneAkeGhly/8dflnCIYbUaZNPPf3jv+Ifv/rX1FRjA0zxgEC2LVnL9387zVSDWUE4GcQGLtQmLVCs3z+DWGQIy8cqygYeHtGpAEYH+CIdAKDYrzX69y8fs1KNfg95HPat283AlgrYHg0DnIvcrCT82HoH/7kFet7GOjHJ3/uGoNQjxTRJ8bC03HeK794bVlYiAJcZHh+RBO5tkA0kgUAcahI7AXw/A9epA6Rg2W8DOL0F2yjcpyUAOPzfkQPZwwfi1qCjwFPPFUeVeTaQSViLQB4PTd+JYM4yMZ0GBoYoLf/8FbFKt/zeYQw/vi7N2l4wNuwHc988XshqgTNPOJKbAWAECuHfRjk3T//KTDPynUAQKiHaIoVQjReh48JMj7GyHXF3Y/VND6IrQA6WREGIwYZnxd7OP89IRrfMSyUBxkfHGb1yCV7tqEisV0JlMM4wmuYxRYugL+9cy5wzNdExS+DKONnfHj/Pikt4XeLklriRmwF0Hv5kpVb5fl8ELslY2JskGFgzF3SGIgsKMpw77+ssPeD2KaAIVFVv/nLN0Kf/5iYv6M5hJmT8/CPKaUfXt6vavHnoM3FoM5D5TXDv3xmCg5ykRmmktfN+4EWAqgmL+N8ZwUQBBlTR+8HWgiAzxjCeKbL+wOmcrgGEfU1VEB5AXDPDBPKufej+POLGDhfnmHgfB28HygvgE52ebca7+8LmGIe0mjez1FaAPyCDIwZtF4Q1fvx/LxWUHnez1FaAFGrcr68DMH4zRZw/pHvHis7v0/hu3+8UFYAXlV5kPdDMNybiz6Xcb0EppP3A2UFwI1zIWDZ16tY9BMMzo0qMBVRUgDcODBM0PX4KOkC9wLywu/dv/hfVFIVJQUQtSrn3o9lZj9v/rbI+zoXfjLKCSBqFQ+497/vky4w3+epQpdFHy+UEwCv4oO8Hzd58nTht4jzPFvxe0/T0O+glACqmZNHSRde0UWXFb9KKCOAahZ94P38er+fYKJGFx1QRgCdHt4fxEq8X+fCT0YJAWCtP8ocHkT1fn6X740VbPLAnUn72N3McUWJjSHYdhX1gs9BdoOIn/fjTiJ+l2+xyo0eSFPO8jF2C10IcV9iLVEiAvDcHOT9fN5/4/o1X+/vjCCWIHKSkCCGoH2MtSb2AkA4jZr7+b1+EIAfO6TzV3qXL//9vPYYxonYC4BX/mFyM8/nfhEDHioLLOjG0CD4KqOJACvAawdOUG5GrSDfHRy0a2c32xdwZxV2+eSlCILfh+88ihOxFkDU27YBjC8XjEFjZLGs1SaP2UJ8dw7HWgCooh2wQSTMqlzrlnJvw15+P2QBrMYOX68LT8UYbx2P9TSwGuPI4RaiCfJoOVqgGMQULupefzwHxuC1sfYgP+fN6/H+0IhYC0D25mpCcxhDyp8ngIgjR52VosKVxFinANnoQyEjgFyAFULk3t4QO4iqAekKu4zjTqwjAO7C6bQ/8CmsoTAFg0djKfjS+8HeBw/F82PqmPH7EKmASt6pNSZsr1flKmKsBYA3s5ql1KhejfPXKhLEHfNJoQnHCCDhGAEkHCOAhGMEkHCMABKOEUDCMQJIOEYACccIIOEYASQcI4CEYwSQcIwAEo4RQMIxAkg4RgAJR+n/HFotmWyWdu15mrZue4zmikUaHRmm/lv/o2KhQEkjUQKA4fd+/YDVMpls2WNTExPWtjPsI8T3SSERAvAzvENLaysd+MaztHvP3kQJQWsBhDE8J2lC0FIA1RieIwth8JO7dOWfH2opBK0EsBqG50AIu1v3WruIEQ10E4IWAlgLw3sBEegmBKUFsF6G5+gkBCUFsJyf2Yc7rDc6CKEmAoDnVrPoEhfDc1QWQk0E8Mij26zKOixxNTxnJUJ4/Cs7qBbURAAHvvms9T96g8Cb4rypKlGNEGr1N6aWBHJHFM9cCXhjrvzjQ8/HYHiIpFZesdoECQF/KyLcesDfUwhgXBzbnI6he/docWmR1gO8MWgP7o9YPyM16GR4Tq3/3nQ6Te3bv1zWBwHcFsec0zH86SAtlEpk0I+GhkZ6tL1d7urH/QBXy09qIIOe1NXX8S5LAHfknsZMhgx6ggjA6HNHgMZGMuhJxu3cVyGA8+UnZSmdMneK6UZdXT01Zl3L5RfTqVQqj2/k3qZNLWTQi0zW7f3C9v2Oq5d9RFZTsxGAbrRsauVdZ/DFEcBp0fLOI5gvNrUYEejCxqYmMQNwLfpexBdLAHYaOCM/CsWYWkB9kPs9vL8H4R/fpJwesSCE1UAsCi2vCk5PTdJkPk8GdcE/w9jY1My7n3QEsOziXlGguWWTSQUK0yxs52H8U47xQYo/KiLBR+KwX+4bHRmhuWLyNk2ojMeyL+gXxn9S7vBK8vifZ2Vxf8vWrVRvloiVoVGs5TyybRvvhk2f450uAdjh4WTZSWJWsK39SyYdKADC/lZhfNiM8bIc+h08y3xxYo84nOL9rW2braIClaUhXmDG1rp5M20SNvIAef+81wMp8kHUA93i8Drvx+XiqckJ+mxmhgy1B17fjGl72tOfYfzuSmN9BQCECI6Kw1mSpocOjhCKhSItLJh7CNYTeDyW7LFqW8HwyPkn7WhekUABACGCnDh8QNKNIxzMEiCE+fk5KpUWaFGIY73uLNIdGDtVl7bu1cDl+kZxxbbRfx8ErvAe88r5nFACcKiUEgyxwVrL8Qv5nEgCAHY06BbtJTLEBWcR77S9oBeayAJwsIXQJdoJYgtHhnXjIj28khvZ8A5VC0BGEgOE0EEPa4UcGVaLvN2Q2+/Yx/PVGl3mcykAxdvW0/cKAAAAAElFTkSuQmCC" alt="Website logo">
            Bookmarks
        </span>
        </a>
        <div class="sm:hidden">
        <button type="button" class="hs-collapse-toggle relative size-9 flex justify-center items-center gap-x-2 rounded-lg border border-gray-200 bg-white text-gray-800 shadow-2xs hover:bg-gray-50 focus:outline-hidden focus:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-transparent dark:border-neutral-700 dark:text-white dark:hover:bg-white/10 dark:focus:bg-white/10" id="hs-navbar-example-collapse" aria-expanded="false" aria-controls="hs-navbar-example" aria-label="Toggle navigation" data-hs-collapse="#hs-navbar-example">
            <svg class="hs-collapse-open:hidden shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" x2="21" y1="6" y2="6"/><line x1="3" x2="21" y1="12" y2="12"/><line x1="3" x2="21" y1="18" y2="18"/></svg>
            <svg class="hs-collapse-open:block hidden shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
            <span class="sr-only">Toggle</span>
        </button>
        </div>
    </div>
    <div id="hs-navbar-example" class="hidden hs-collapse overflow-hidden transition-all duration-300 basis-full grow sm:block" aria-labelledby="hs-navbar-example-collapse">
        <div class="flex flex-col gap-5 mt-5 sm:flex-row sm:items-center sm:justify-end sm:mt-0 sm:ps-5">
        <a type="button" class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-transparent bg-white text-gray-800 hover:bg-gray-200 focus:outline-hidden focus:bg-gray-200 disabled:opacity-50 dark:bg-neutral-800 dark:text-white dark:hover:bg-neutral-700  disabled:pointer-events-none"
            href="https://lianglu.uk" aria-label="Button">
            個人網站
        </a>
        </div>
    </div>
    </nav>
</header>
"""

search_block_html = "<div class='py-2'></div>"
"""\
<div class="px-2 py-5 md:px-1 md:py-4 lg:px-0 lg:py-6">
    <div class="w-full bg-linear-to-bl from-brown-50 to-brown-300 dark:from-brown-700 dark:to-brown-900 rounded-lg p-2 md:p-4 lg:p-8">
        <div class="w-fill text-center">
        <h1 class="text-2xl font-bold mb-4 text-neutral-700 dark:text-neutral-100">Mixer Search</h1>
        </div>
        <div class="w-full flex gap-2 flex-wrap md:flex-nowrap flex-col md:flex-row">
        <select data-hs-select='{
            "placeholder": "Select option...",
            "toggleTag": "<button type="button" aria-expanded="false"></button>",
            "toggleClasses": "hs-select-disabled:pointer-events-none hs-select-disabled:opacity-50 relative py-3 ps-4 pe-9 flex gap-x-2 text-nowrap w-full cursor-pointer bg-white border border-gray-200 rounded-lg text-start text-sm focus:outline-hidden focus:ring-2 focus:ring-brown-500 dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:focus:outline-hidden dark:focus:ring-1 dark:focus:ring-neutral-600",
            "dropdownClasses": "mt-2 z-50 w-full max-h-72 p-1 space-y-0.5 bg-white border border-gray-200 rounded-lg overflow-hidden overflow-y-auto [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-track]:bg-gray-100 [&::-webkit-scrollbar-thumb]:bg-gray-300 dark:[&::-webkit-scrollbar-track]:bg-neutral-700 dark:[&::-webkit-scrollbar-thumb]:bg-neutral-500 dark:bg-neutral-900 dark:border-neutral-700",
            "optionClasses": "py-2 px-4 w-full text-sm text-gray-800 cursor-pointer hover:bg-gray-100 rounded-lg focus:outline-hidden focus:bg-gray-100 hs-select-disabled:pointer-events-none hs-select-disabled:opacity-50 dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:text-neutral-200 dark:focus:bg-neutral-800",
            "optionTemplate": "<div class="flex justify-between items-center w-full gap-2"><span data-title></span><span class="hidden hs-selected:block"><svg class="shrink-0 size-3.5 text-brown-600 dark:text-brown-500 " xmlns="http:.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></span></div>",
            "extraMarkup": "<div class="absolute top-1/2 end-3 -translate-y-1/2"><svg class="shrink-0 size-3.5 text-gray-500 dark:text-neutral-500 " xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m7 15 5 5 5-5"/><path d="m7 9 5-5 5 5"/></svg></div>"
        }' class="hidden">
            <option value="Google" selected>Google</option>
            <option value="ChatGPT" >ChatGPT</option>
            <option value="Felo">Felo.ai</option>
        </select>
        <!-- End Select -->
        <input type="text" class="w-full px-4 py-2 text-gray-700 dark:text-neutral-50 bg-white border dark:bg-neutral-900 border-gray-300 dark:border-neutral-700 rounded-lg focus:outline-none focus:border-brown-500" placeholder="Search...">
        <button type="submit" class="px-4 py-2 bg-brown-400 dark:bg-neutral-800 text-brown-900 dark:text-neutral-100 hover:bg-neutral-950 rounded-lg focus:outline-none">
            Seaarch
        </button>
        </div>
    </div>
</div>
"""

totop_html = """
<button id="toTop" class="fixed bottom-24 right-8 hidden border-0 drop-shadow-lg">
    <div class="size-16 btn bg-primary hover:bg-primaryhover rounded-full overflow-hidden flex items-center justify-center">
    <svg xmlns="http://www.w3.org/2000/svg"  class="w-8 h-8" fill="#FFFFFF"  viewBox="0 0 16 16"><path fill-rule="evenodd"  d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5" /></svg>
    </div>
</button>
"""

totop_js = """
// 監聽滾動事件
window.addEventListener('scroll', function () {
    const toTopBtn = document.getElementById('toTop');

    // 當滾動超過 100px 時顯示按鈕
    if (window.scrollY > 100) {
        toTopBtn.style.display = 'block';
    } else {
        toTopBtn.style.display = 'none';
    }
});

// 點擊按鈕回到頂部
document.getElementById('toTop').addEventListener('click', function () {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
"""

full_html = f"""\
<!doctype html>
<html>
    {html_head}
    <body class="bg-gray-100 dark:bg-neutral-900">
        {header_html}
        <div class="max-w-[85rem] container mx-auto px-2">
            {search_block_html}
            <div>
                <div id="hs-scroll-nav-tabs-centered" class="relative border-b border-gray-200 overflow-hidden dark:border-neutral-700" data-hs-scroll-nav="">
                    <nav id="hs-tabs-centered" class="hs-scroll-nav-body flex gap-x-1 snap-x snap-mandatory overflow-x-auto [&::-webkit-scrollbar]:h-0" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
                    {tabs_nav_html}
                    </nav>
                    <!-- Arrows -->
                    <button type="button" class="hidden md:flex hs-scroll-nav-prev hs-scroll-nav-disabled:hidden hs-scroll-nav-disabled:pointer-events-none absolute top-1/2 start-0 z-10 shrink-0 justify-center items-center size-9 bg-white text-gray-800 rounded-full -translate-y-1/2 hover:bg-gray-100 focus:outline-hidden focus:bg-gray-100 dark:text-white dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:focus:bg-neutral-800">
                    <svg class="shrink-0 size-5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="m15 18-6-6 6-6"></path>
                    </svg>
                    <span class="sr-only">Previous</span>
                    </button>
                    <button type="button" class="hidden md:flex hs-scroll-nav-next hs-scroll-nav-disabled:hidden hs-scroll-nav-disabled:pointer-events-none absolute top-1/2 end-0 z-10 shrink-0 justify-center items-center size-9 bg-white text-gray-800 rounded-full -translate-y-1/2 hover:bg-gray-100 focus:outline-hidden focus:bg-gray-100 dark:text-white dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:focus:bg-neutral-800">
                    <span class="sr-only">Next</span>
                    <svg class="shrink-0 size-5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="m9 18 6-6-6-6"></path>
                    </svg>
                    </button>
                    <!-- End Arrows -->
                </div>
                <div class="mt-3">
                    {tabs_content_html}
                </div>
            </div>
        </div>

        {totop_html}
        <script>
            {totop_js}
        </script>
    </body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Done!")

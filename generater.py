import toml
import python.checker as checker

################################################################################################
head_html = """
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pinmark・Liang 的常用書籤</title>
<link rel="icon" href="favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="favicon.png">
<link rel="apple-touch-startup-image" href="favicon.png">
<meta name="apple-mobile-web-app-title" content="Pinmark">
<link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.23/dist/full.min.css" rel="stylesheet" type="text/css" />
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    primary: '#7D6D69',
                    primaryhover: '#574844',
                }
            }
        }
    }
</script>
"""
page_css = """
#bookmark-page {
    display: block;
}

#search-page {
    display: none;
}
.body {
    min-height: calc(100vh - 72px) !important;
}
"""


navbar_html = """
<div class="navbar bg-base-100 drop-shadow">
    <div class="flex-1">
        <a class="btn btn-ghost text-xl">
            <image src="/favicon.png" class="h-8" />
            Bookmark Webs
        </a>
    </div>
    <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
            <li><a href="https://lianglu.uk" target="_blank">作者網站</a></li>
        </ul>
    </div>
</div>
"""

search_html = """
<div class="body grid content-center justify-items-center">
    <div class="p-5 w-full max-w-lg">
        <div class="card bg-white dark:bg-zinc-900 shadow-lg">
            <div class="card-body">
                <h2 class="card-title mb-3">Search</h2>
                <select class="select select-bordered w-full mb-4" id="select_search_engine">
                    <option selected>Google</option>
                    <option>ChatGPT</option>
                    <option>Felo.ai</option>
                </select>
                <textarea class="textarea textarea-bordered w-full mb-4" placeholder="Search text."
                    id="textinput_search_text"></textarea>
                <button class="btn bg-primary hover:bg-primaryhover rounded-full text-white w-full" onclick="activate_search()">Search</button>
            </div>
        </div>
    </div>
</div>
"""

search_js = """
<!--Search Function activate-->
const select_search_engine = document.getElementById('select_search_engine');
const textinput_search_text = document.getElementById('textinput_search_text');
function activate_search() {
    const search_engine = select_search_engine.value;
    const search_text = textinput_search_text.value;
    if (search_engine == 'Google') {
        window.open(`https://www.google.com/search?q=${search_text}`);
    } else if (search_engine == 'ChatGPT') {
        window.open(`https://chatgpt.com/search?q=${search_text}`);
    } else if (search_engine == 'Felo.ai') {
        window.open(`https://felo.ai/search?q=${search_text}`);
    }
}
"""

switch_js = """
const bookmarkTab = document.getElementById('bookmark-tab');
const searchTab = document.getElementById('search-tab');
const bookmarkPage = document.getElementById('bookmark-page');
const searchPage = document.getElementById('search-page');

bookmarkTab.addEventListener('click', () => {
    // 切换到书签页面
    bookmarkPage.style.display = 'block';
    searchPage.style.display = 'none';

    // 更新按钮状态
    bookmarkTab.classList.add('active');
    searchTab.classList.remove('active');
});

searchTab.addEventListener('click', () => {
    // 切换到搜索页面 
    bookmarkPage.style.display = 'none';
    searchPage.style.display = 'block';

    // 更新按钮状态
    searchTab.classList.add('active');
    bookmarkTab.classList.remove('active');
});
"""

totop_html = """
<button id="toTop" class="fixed bottom-24 right-8 hidden border-0 drop-shadow-2xl">
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


################################################################################################
def read_toml(file_path):
    try:
        data = toml.load(file_path)
        checker.data_checker(data)
        return data
    except Exception as e:
        raise ImportError(f"Error reading file: {file_path}. {e}")


file_path = "bookmarks.toml"
bookmark_datas = read_toml(file_path)

# print(bookmark_datas)
bookmark_html_output = ""
for main_index, bookmark_category in enumerate(bookmark_datas):
    bookmark_html_output += f"""
    <input type="radio" name="bookmatks_tabs" role="tab" class="tab text-nowrap text-xl pb-8" aria-label="{bookmark_category}" {"checked='checked'" if main_index == 0 else ''}/>
    <div role="panel_bookmatks_tabs" class="tab-content py-4">
    """
    for subtitle_index, subtitle in enumerate(bookmark_datas[bookmark_category]):
        bookmark_html_output += f"""
        <h3 class="text-3xl font-bold my-3">{subtitle}</h3>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 2xl:grid-cols-6 gap-4 mb-12">
        """
        for bookmark_item in bookmark_datas[bookmark_category][subtitle]:
            bookmark_html_output += f"""
            <a href="{bookmark_item['url']}" class="block">
                <div class="card bg-base-100 shadow-none hover:shadow-md hover:bg-primaryhover hover:text-white h-full">
                    <div class="card-body p-6 pt-5">
                        <div width="36px" height="36px" style="background-image: url('{bookmark_item['icon']}')"
                            class="h-8 w-8 bg-contain bg-no-repeat bg-center rounded border-2 border-white bg-white"></div>
                        <p class="card-title">{bookmark_item['title']}</p>
                        <p>{bookmark_item['caption']}</p>
                    </div>
                </div>
            </a>
            """
        bookmark_html_output += "</div>"
    bookmark_html_output += "</div>"

################################################################################################
full_html = f"""
<!doctype html>
<html lang="zh">

<head>
    {head_html}
    <style>{page_css}</style>
</head>

<body class="bg-slate-100 dark:bg-zinc-800">
    {navbar_html}

    <div class="body">
        <div id="bookmark-page">
            <div class="container-fuild body mx-auto pt-4 pb-20 px-4 sm:px-8 md-px-10 lg:px-12 mb-1">
                <div role="tablist" class="tabs tabs-bordered mt-4">
                    {bookmark_html_output}
                </div>
            </div>
        </div>
        <div id="search-page">
            {search_html}
        </div>
    </div>
    <div class="btm-nav">
        <button id="bookmark-tab" class="active">
            <svg class="h-5 w-5" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M10 44C8.89543 44 8 43.1046 8 42V6C8 4.89543 8.89543 4 10 4H38C39.1046 4 40 4.89543 40 6V42C40 43.1046 39.1046 44 38 44H10Z"
                    fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" />
                <path fill-rule="evenodd" clip-rule="evenodd" d="M21 22V4H33V22L27 15.7273L21 22Z" fill="none"
                    stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M10 4H38" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                    stroke-linejoin="round" />
            </svg>
        </button>
        <button id="search-tab">
            <svg class="h-5 w-5" fill="none" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M21 38C30.3888 38 38 30.3888 38 21C38 11.6112 30.3888 4 21 4C11.6112 4 4 11.6112 4 21C4 30.3888 11.6112 38 21 38Z"
                    fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" />
                <path d="M26.657 14.3431C25.2093 12.8954 23.2093 12 21.0001 12C18.791 12 16.791 12.8954 15.3433 14.3431"
                    stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M33.2216 33.2217L41.7069 41.707" stroke="currentColor" stroke-width="3" stroke-linecap="round"
                    stroke-linejoin="round" />
            </svg>
        </button>
    </div>

    {totop_html}

    <script>
        {switch_js}

        {search_js}

        {totop_js}
    </script>
</body>

</html>
"""

# Write to file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Done!")

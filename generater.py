import toml
import python.checker as checker

################################################################################################
head_html = """
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pinmark・Liang 的常用書籤</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<link rel="icon" href="favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="favicon.png">
<link rel="apple-touch-startup-image" href="favicon.png">
<meta name="apple-mobile-web-app-title" content="Pinmark">
"""
page_css = """
    .nav-pills {
        --bs-nav-pills-border-radius: var(--bs-border-radius);
        --bs-nav-pills-link-active-color: #fff;
        --bs-nav-pills-link-active-bg: #7D6D69;
    }

    :root {
        --bs-link-color: #7D6D69;
        --bs-link-hover-color: #302624;
    }

    .btn-primary {
        --bs-btn-bg: #7D6D69;
        --bs-btn-border-color: #7D6D69;
        --bs-btn-hover-bg: #302624;
        --bs-btn-hover-border-color: #302624;
    }

    .form-control:focus {
        border-color: #7D6D6900;
        box-shadow: 0 0 0 .25rem rgba(38, 92, 16, 0);
    }

    .hover-link {
        scale: 1;
    }

    .hover-link:hover {
        transform: scale(1.02);
        transition-duration: 0.5s;
        box-shadow: 2px 2px 8px rgba(56, 55, 55, 0.137);
    }

    .link_div {
        padding-top: 12px;
    }

    .link_title {
        font-size: 1rem;
    }

    .link_caption {
        padding-top: 4px;
        margin: 0px;
        font-size: 0.8rem;
        opacity: 0.7;
    }

    #googleSearchInput {
        border: 0;
    }
"""


navbar_html = """
<nav class="navbar fixed-top bg-body-tertiary shadow" id="topNav">
    <div class="container-fluid px-4">
        <a class="navbar-brand" href="#topNav">
            <img src="./assets/imgs/header_img.png" height="52px;">
        </a>
        <div class="d-flex">
            <a href="http://lianglu.uk" target="_blank" rel="noopener noreferrer" class="btn btn-light">
                作者網站
            </a>
        </div>
    </div>
</nav>
"""

search_html = """
<div class="container-fluid" style="margin-top: 120px;">
    <div class="row px-4">
        <div class="col-12">
            <ul class="nav nav-underline" id="myTab" role="tablist">
                <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="home-tab" data-bs-toggle="tab"
                        data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane"
                        aria-selected="true">Google</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="profile-tab" data-bs-toggle="tab"
                        data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane"
                        aria-selected="false">Felo (AI Search)</button>
                </li>
            </ul>
            <div class="tab-content py-3" id="myTabContent">
                <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab"
                    tabindex="0">
                    <div class="row">
                        <div class="col-12 p-2 border border-1 bg-body rounded-pill overflow-hidden">
                            <form id="searchFormG" class="d-flex" onsubmit="handleSearch(event,'google')">
                                <input type="text" class="bg-body form-control me-2" placeholder="Google 快速搜尋"
                                    id="googleSearchInput" required>
                                <button class="btn btn-primary rounded-pill text-nowrap" type="submit">
                                    Search
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab"
                    tabindex="0">
                    <div class="row">
                        <div class="col-12 p-2 border border-1 bg-body rounded-pill overflow-hidden">
                            <form id="searchFormF" class="d-flex" onsubmit="handleSearch(event,'felo')">
                                <input type="text" class="bg-body form-control me-2" placeholder="Felo AI 快速搜尋"
                                    id="feloSearchInput" required>
                                <button class="btn btn-primary rounded-pill text-nowrap" type="submit">
                                    Search
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

search_js = """
function handleSearch(event, engine) {
    id_block = "";
    url = "";
    if (engine == "google") {
        id_block = "googleSearchInput";
        url = "https://www.google.com/search";
    } else if (engine == "felo") {
        id_block = "feloSearchInput";
        url = "https://felo.ai/zh-Hant/search";
    }
    event.preventDefault();
    const searchText = document.getElementById(id_block).value;
    if (searchText.trim() !== '') {
        const googleSearchUrl = `${url}?q=${encodeURIComponent(searchText)}`;
        window.open(googleSearchUrl, '_blank'); // 使用 window.open 來開啟新分頁
    }
}
"""

totop_html = """
<button id="toTop" class="position-fixed bottom-0 start-0 m-4 border-0 shadow-md"
style="display: none; background-color: #30262400;">
    <div style="width: 48px;height: 48px;"
        class="btn btn-primary rounded-circle d-flex justify-content-center align-items-center">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-arrow-up"
            viewBox="0 0 16 16">
            <path fill-rule="evenodd"
                d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5" />
        </svg>
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


def get_category_tab_btn_html(category_datas) -> str:
    from html import escape

    out = []
    is_first = True

    for category_name, category_data in category_datas.items():
        # Replace spaces with hyphens and escape the category name for HTML
        category_id = escape(category_name).replace(" ", "-")

        button = f"""
        <button class="nav-link rounded-pill mb-2 {'active' if is_first else ''}" 
                id="tab-{category_id}-tab" 
                data-bs-toggle="pill"
                data-bs-target="#tab-{category_id}" 
                type="button" 
                role="tab" 
                aria-controls="tab-{category_id}"
                aria-selected="{str(is_first).lower()}">
            {escape(category_name)}
        </button>"""

        out.append(button)
        is_first = False

    return "".join(out)


def get_category_tab_html(category_datas) -> str:
    from html import escape

    out = []
    is_first = True

    for category_name, category_data in category_datas.items():
        # Replace spaces with hyphens and escape the category name for HTML
        category_id = escape(category_name).replace(" ", "-")

        subcategories_html = "".join(
            get_subcategory_html(subcat_name, subcat_data)
            for subcat_name, subcat_data in category_data.items()
        )

        tab_content = f"""
        <div class="tab-pane fade{' show active' if is_first else ''}" 
            id="tab-{category_id}" 
            role="tabpanel"
            aria-labelledby="tab-{category_id}-tab" 
            tabindex="0">
            <div class="container-fluid">
                {subcategories_html}
            </div>
        </div>"""

        out.append(tab_content)
        is_first = False

    return "".join(out)


def get_subcategory_html(subcategory_name: str, items: list) -> str:
    return f"""<div class="row g-3 pb-5">
        <div class="col-12">
            <h2 class="pb-0">{subcategory_name}</h2>
        </div>
        {''.join(get_item_html(item) for item in items)}
    </div>"""


def get_item_html(item: dict) -> str:
    return f"""
    <div class="col-12 col-md-6 col-lg-3 col-xl-2">
        <a href="{item.get("url")}" class="text-reset text-decoration-none">
            <div class="card hover-link h-100">
                <div class="card-body">
                    <div class="col-auto">
                        <img src="{item.get("icon")}" width="32px" class="rounded">
                    </div>
                    <div class="col">
                        <div class="link_div">
                            <strong class="link_title">{item.get("title")}</strong>
                            <p class="link_caption">{item.get("caption")}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </a>
    </div>
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

################################################################################################
full_html = f"""
<!doctype html>
<html lang="zh">

<head>
    {head_html}
    <style>{page_css}</style>
</head>

<body style="background-image: url('https://free-paper-texture.com/p/p0435/p0435_m.jpg');">
    {navbar_html}

    {search_html}

    <div class="container-fluid py-4 px-lg-4">
        <div class="d-flex align-items-start">
            <div class="nav flex-column nav-pills me-3">
                {get_category_tab_btn_html(bookmark_datas)}
            </div>
            <div class="tab-content px-4 w-100" id="pills-tabContent">
                {get_category_tab_html(bookmark_datas)}
            </div>
        </div>
    </div>

    {totop_html}


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
    <script>
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

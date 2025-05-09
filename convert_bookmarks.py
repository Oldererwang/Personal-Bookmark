import re
from bs4 import BeautifulSoup
import sys

def convert_bookmarks_to_toml(html_file, toml_file):
    # 读取HTML文件
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"成功读取HTML文件，大小: {len(content)} 字节")
    except Exception as e:
        print(f"读取HTML文件时出错: {e}")
        return
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # 保存HTML到文件以便检查结构
    with open("debug_html.txt", "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))
    print("已保存完整HTML到debug_html.txt用于调试")
    
    # 初始化TOML数据结构
    toml_data = {}
    
    # 直接找到所有分类和链接
    # 首先找到所有H3标签作为分类
    categories = soup.find_all('h3')
    print(f"找到 {len(categories)} 个H3标签")
    
    for category in categories:
        category_name = category.text.strip()
        print(f"处理分类: {category_name}")
        
        if '书签栏' in category_name:
            print("跳过书签栏本身")
            continue
        
        # 初始化分类
        if category_name not in toml_data:
            toml_data[category_name] = {}
        
        # 找到分类后面的DL标签（包含链接或子分类）
        next_element = category.next_sibling
        while next_element and (not hasattr(next_element, 'name') or next_element.name != 'dl'):
            next_element = next_element.next_sibling
        
        category_dl = next_element
        if not category_dl or category_dl.name != 'dl':
            print(f"  未找到分类 '{category_name}' 后的DL标签")
            # 尝试查找p标签中的dl
            parent = category.parent
            if parent and parent.name == 'dt':
                parent_sibling = parent.next_sibling
                while parent_sibling and (not hasattr(parent_sibling, 'name') or parent_sibling.name != 'dl'):
                    parent_sibling = parent_sibling.next_sibling
                category_dl = parent_sibling
            
            if not category_dl:
                print(f"  无法找到分类 '{category_name}' 的子元素")
                continue
        
        # 检查此分类下是否有子分类
        sub_h3s = category_dl.find_all('h3', recursive=False)
        
        if sub_h3s:
            # 有子分类
            print(f"  分类 '{category_name}' 有嵌套子分类")
            
            # 从内部DL和DT里找出所有子分类
            for dt in category_dl.find_all('dt'):
                sub_h3 = dt.find('h3')
                if sub_h3:
                    sub_name = sub_h3.text.strip()
                    print(f"    找到子分类: {sub_name}")
                    
                    # 初始化子分类
                    if sub_name not in toml_data[category_name]:
                        toml_data[category_name][sub_name] = []
                    
                    # 找到子分类对应的DL
                    sub_dl = None
                    next_element = dt.next_sibling
                    while next_element and (not hasattr(next_element, 'name') or next_element.name != 'dl'):
                        next_element = next_element.next_sibling
                    sub_dl = next_element
                    
                    if not sub_dl:
                        print(f"    未找到子分类 '{sub_name}' 的DL")
                        continue
                    
                    # 获取子分类下的所有书签
                    bookmarks = sub_dl.find_all('a')
                    print(f"    子分类 '{sub_name}' 有 {len(bookmarks)} 个书签")
                    
                    for link in bookmarks:
                        title = link.text.strip()
                        url = link.get('href', '')
                        
                        # 尝试获取图标
                        icon = ""
                        if link.has_attr('ICON'):
                            icon = link['ICON']
                        elif link.has_attr('icon'):
                            icon = link['icon']
                        
                        bookmark = {
                            "title": title,
                            "caption": "",  # 默认为空
                            "url": url,
                            "icon": icon
                        }
                        toml_data[category_name][sub_name].append(bookmark)
        else:
            # 没有子分类，直接获取书签
            bookmarks = category_dl.find_all('a')
            print(f"  分类 '{category_name}' 没有子分类，直接有 {len(bookmarks)} 个书签")
            
            # 使用"默认"作为子分类名
            if "默认" not in toml_data[category_name]:
                toml_data[category_name]["默认"] = []
            
            for link in bookmarks:
                title = link.text.strip()
                url = link.get('href', '')
                
                # 尝试获取图标
                icon = ""
                if link.has_attr('ICON'):
                    icon = link['ICON']
                elif link.has_attr('icon'):
                    icon = link['icon']
                
                bookmark = {
                    "title": title,
                    "caption": "",  # 默认为空
                    "url": url,
                    "icon": icon
                }
                toml_data[category_name]["默认"].append(bookmark)
    
    # 检查是否有数据
    if not toml_data:
        print("未能提取任何数据到TOML结构中")
        return
    
    # 将数据写入TOML文件
    formatted_toml = ""
    for category, sub_categories in toml_data.items():
        formatted_toml += f'["{category}"]\n'
        for sub_category, bookmarks in sub_categories.items():
            for bookmark in bookmarks:
                formatted_toml += f'[["{category}"."{sub_category}"]]\n'
                
                # 转义特殊字符
                title = bookmark["title"].replace('"', '\\"').replace('\n', ' ')
                url = bookmark["url"].replace('"', '\\"')
                caption = bookmark["caption"].replace('"', '\\"')
                icon = bookmark["icon"].replace('"', '\\"')
                
                formatted_toml += f'title = "{title}"\n'
                formatted_toml += f'caption = "{caption}"\n'
                formatted_toml += f'url = "{url}"\n'
                formatted_toml += f'icon = "{icon}"\n\n'
    
    try:
        with open(toml_file, 'w', encoding='utf-8') as f:
            f.write(formatted_toml)
        print(f"转换完成！生成的TOML文件大小: {len(formatted_toml)} 字节")
    except Exception as e:
        print(f"写入TOML文件时出错: {e}")
    
    if len(formatted_toml) == 0:
        print("警告: 生成的TOML内容为空")


if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("用法: python script.py 输入.html文件 输出.toml文件")
    #     sys.exit(1)
    
    html_file = "bookmarks_test.html"
    toml_file = "bookmarks.toml"
    convert_bookmarks_to_toml(html_file, toml_file)

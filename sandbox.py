import tkinter
import tkinter.ttk
import xml.etree.ElementTree

xml_document = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''


def layout_children(tree_view, element_tree, dictionary_key, parent_tag):
    for child_element in element_tree:
        tree_view.insert(parent_tag, 'end', text=child_element.attrib[dictionary_key])
    return tree_view


def recursive_layout(tree_view, element_tree):
    for child_element in element_tree:
        recursive_layout(tree_view, child_element)
    tree_view.insert('', text=element_tree.attrib)


root_element = xml.etree.ElementTree.fromstring(xml_document)

root = tkinter.Tk()
root.title("Sandbox")

mainframe = tkinter.ttk.Frame(root)
mainframe.pack()

normal_tree = tkinter.ttk.Treeview(mainframe)
normal_tree.pack()

normal_tree.insert('', 0, root_element.tag, text='Example')

# current_index = 0
# for child_element in root_element:
#     normal_tree.insert(root_element.tag, current_index, text=child_element.attrib)

# normal_tree = layout_children(normal_tree, root_element, 'name', root_element.tag)
layout_children(normal_tree, root_element, 'name', root_element.tag)

root.mainloop()

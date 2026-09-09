# import os
# import ast

# COMPONENTS_DIR = "src/components"  # adjust to your project

# def parse_class_from_file(filepath: str):
#     """Parse a Python file using AST and return class info."""
#     with open(filepath, "r", encoding="utf-8") as f:
#         tree = ast.parse(f.read(), filename=filepath)

#     classes = []
#     for node in tree.body:
#         if isinstance(node, ast.ClassDef):
#             cls_name = node.name
#             attributes = {}
#             methods = []

#             # Class-level annotations
#             for stmt in node.body:
#                 if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
#                     attr_name = stmt.target.id
#                     attr_type = ast.unparse(stmt.annotation) if stmt.annotation else "Any"
#                     attributes[attr_name] = attr_type

#             # Methods
#             for stmt in node.body:
#                 if isinstance(stmt, ast.FunctionDef):
#                     method_name = stmt.name
#                     params = []
#                     for arg in stmt.args.args:
#                         if arg.arg == "self":
#                             continue
#                         param_type = ast.unparse(arg.annotation) if arg.annotation else None
#                         params.append(f"{arg.arg}: {param_type}" if param_type else arg.arg)
#                     ret_type = ast.unparse(stmt.returns) if stmt.returns else None
#                     methods.append((method_name, params, ret_type))

#             classes.append({"name": cls_name, "attributes": attributes, "methods": methods})

#     return classes


# def generate_blueprint_stub(filepath: str):
#     classes = parse_class_from_file(filepath)
#     if not classes:
#         return

#     folder = os.path.dirname(filepath)

#     for cls in classes:
#         lines = [f"class {cls['name']}Blueprint:"]
#         # Attributes
#         for attr, typ in cls["attributes"].items():
#             lines.append(f"    {attr}: {typ}")
#         if not cls["attributes"] and not cls["methods"]:
#             lines.append("    pass")
#         # Methods
#         for method_name, params, ret_type in cls["methods"]:
#             param_str = ", ".join(params)
#             ret_str = f" -> {ret_type}" if ret_type else ""
#             lines.append(f"    def {method_name}(self, {param_str}){ret_str}: ...")

#         # Write the stub in the same folder as the logic.py
#         output_file = os.path.join(folder, "logicblueprint.py")
#         with open(output_file, "w", encoding="utf-8") as f:
#             f.write("\n".join(lines))
#         print(f"Generated {output_file}")


# # Walk all component folders
# for root, dirs, files in os.walk(COMPONENTS_DIR):
#     for file in files:
#         if file == "logic.py":
#             generate_blueprint_stub(os.path.join(root, file))



# import os
# import ast

# COMPONENTS_DIR = "src/components/web"  # adjust to your project

# def parse_class_from_file(filepath: str):
#     """Parse a Python file using AST and return class info including method docstrings."""
#     with open(filepath, "r", encoding="utf-8") as f:
#         tree = ast.parse(f.read(), filename=filepath)

#     classes = []
#     for node in tree.body:
#         if isinstance(node, ast.ClassDef):
#             cls_name = node.name
#             attributes = {}
#             methods = []

#             # Class-level annotations
#             for stmt in node.body:
#                 if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
#                     attr_name = stmt.target.id
#                     attr_type = ast.unparse(stmt.annotation) if stmt.annotation else "Any"
#                     attributes[attr_name] = attr_type

#             # Methods
#             for stmt in node.body:
#                 if isinstance(stmt, ast.FunctionDef):
#                     method_name = stmt.name
#                     params = []
#                     param_docs = []
#                     for arg in stmt.args.args:
#                         if arg.arg == "self":
#                             continue
#                         param_type = ast.unparse(arg.annotation) if arg.annotation else None
#                         params.append(f"{arg.arg}: {param_type}")
#                         param_docs.append(f"    {arg.arg} ({param_type})")

#                     ret_type = ast.unparse(stmt.returns) if stmt.returns else None

#                     # Build auto docstring
#                     docstring_lines = []
#                     if param_docs:
#                         docstring_lines.append("    Parameters:")
#                         docstring_lines.extend(param_docs)
#                     docstring_lines.append(f"    Returns:\n        {ret_type}")

#                     methods.append((method_name, params, ret_type, "\n".join(docstring_lines)))

#             # Capture class docstring
#             class_doc = ast.get_docstring(node) or f"{cls_name} logic class."
#             classes.append({
#                 "name": cls_name,
#                 "attributes": attributes,
#                 "methods": methods,
#                 "docstring": class_doc
#             })

#     return classes


# def generate_blueprint_stub(filepath: str):
#     classes = parse_class_from_file(filepath)
#     if not classes:
#         return

#     folder = os.path.dirname(filepath)

#     for cls in classes:
#         lines = []
#         cls_name = cls["name"]
#         lines.append(f"class {cls_name}Blueprint:")

#         # Class docstring
#         if cls["docstring"]:
#             lines.append(f'    """{cls["docstring"]}"""')

#         # Attributes
#         for attr, typ in cls["attributes"].items():
#             # Leave blank if no type specified
#             attr_type = typ if typ != "Any" else ""
#             lines.append(f"    {attr}: {attr_type}" if attr_type else f"    {attr}")

#         if not cls["attributes"] and not cls["methods"]:
#             lines.append("    pass")

#         # Methods with auto-generated docstrings
#         for method_name, params, ret_type, docstring in cls["methods"]:
#             # Build function signature
#             param_list = []
#             for param in params:
#                 if ":" in param:
#                     name, typ = param.split(":")
#                     typ = typ.strip()
#                     param_list.append(f"{name}: {typ}" if typ else name)
#                 else:
#                     param_list.append(param)
#             signature = f"(self, {', '.join(param_list)})" if param_list else "(self)"
#             ret_str = f" -> {ret_type}" if ret_type and ret_type != "Any" else ""

#             # Build properly indented docstring
#             doc_lines = []
#             if param_list:
#                 doc_lines.append("Parameters:")
#                 for param in param_list:
#                     if ":" in param:
#                         name, typ = param.split(":")
#                         typ = typ.strip()
#                         doc_lines.append(f"    {name} ({typ})" if typ else f"    {name}")
#                     else:
#                         doc_lines.append(f"    {param}")

#             doc_lines.append("Returns:")
#             if ret_type and ret_type != "Any":
#                 doc_lines.append(f"    {ret_type}")

#             indented_docstring = "\n".join(f"        {line}" for line in doc_lines)

#             # Write function and docstring
#             lines.append(f"    def {method_name}{signature}{ret_str}:")
#             lines.append('        """')
#             lines.append(indented_docstring)
#             lines.append('        """')
#             lines.append("        ...")

#         # Write the stub in the same folder as logic.py
#         output_file = os.path.join(folder, "logicblueprint.py")
#         with open(output_file, "w", encoding="utf-8") as f:
#             f.write("\n".join(lines))
#         print(f"Generated {output_file}")




# # Walk all component folders
# for root, dirs, files in os.walk(COMPONENTS_DIR):
#     for file in files:
#         if file == "logic.py":
#             generate_blueprint_stub(os.path.join(root, file))



import os
import ast
from typing import *

COMPONENTS_DIR = "src/components/temp"  # adjust to your project



def parse_class_from_file(filepath: str):
    """Parse a Python file using AST and return class info including method docstrings and instance attributes."""
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=filepath)

    classes = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            cls_name = node.name
            attributes = {}

            # Class-level annotated attributes
            for stmt in node.body:
                if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                    attr_name = stmt.target.id
                    attr_type = ast.unparse(stmt.annotation) if stmt.annotation else None
                    attributes[attr_name] = attr_type
                elif isinstance(stmt, ast.Assign):
                    for target in stmt.targets:
                        if isinstance(target, ast.Name) and target.id not in attributes:
                            attributes[target.id] = None  # untyped

            # Scan __init__ for self.<attr> assignments
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
                    for substmt in stmt.body:
                        if isinstance(substmt, ast.Assign):
                            for target in substmt.targets:
                                if isinstance(target, ast.Attribute):
                                    if isinstance(target.value, ast.Name) and target.value.id == "self":
                                        attr_name = target.attr
                                        if attr_name not in attributes:
                                            # Include type if annotated (Python 3.6+ style)
                                            typ = getattr(substmt, "annotation", None)
                                            attributes[attr_name] = ast.unparse(typ) if typ else None

            # Methods
            methods = []
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDef):
                    method_name = stmt.name
                    existing_doc = ast.get_docstring(stmt) or ""

                    # Exclude 'self'
                    args = [arg for arg in stmt.args.args if arg.arg != "self"]
                    num_args = len(args)
                    num_defaults = len(stmt.args.defaults)
                    defaults = [None] * (num_args - num_defaults) + [ast.unparse(d) for d in stmt.args.defaults]

                    # Build parameters: (name, type, default)
                    params: List[Tuple[str, Optional[str], Optional[str]]] = []
                    for i, arg in enumerate(args):
                        typ = ast.unparse(arg.annotation) if arg.annotation else None
                        default_val = defaults[i]
                        params.append((arg.arg, typ, default_val))

                    ret_type = ast.unparse(stmt.returns) if stmt.returns else None

                    # Build docstring
                    doc_lines = []
                    if params:
                        doc_lines.append("Parameters:")
                        for name, typ, _ in params:
                            doc_lines.append(f"    {name} ({typ})" if typ else f"    {name}")

                    if ret_type:
                        doc_lines.append("Returns:")
                        doc_lines.append(f"    {ret_type}")

                    if existing_doc:
                        if doc_lines:
                            doc_lines.append("")  # blank line
                        doc_lines.append("Implementation description:")
                        for line in existing_doc.splitlines():
                            doc_lines.append(f"    {line}")

                    combined_docstring = "\n".join(doc_lines)
                    methods.append((method_name, params, ret_type, combined_docstring))

            class_doc = ast.get_docstring(node) or f"{cls_name} logic class."
            classes.append({
                "name": cls_name,
                "attributes": attributes,
                "methods": methods,
                "docstring": class_doc
            })

    return classes


def generate_blueprint_stub(filepath: str):
    classes = parse_class_from_file(filepath)
    if not classes:
        return

    folder = os.path.dirname(filepath)

    for cls in classes:
        lines = []
        cls_name = cls["name"]
        lines.append(f"class {cls_name}Blueprint:")

        # Class docstring
        if cls["docstring"]:
            lines.append(f'    """{cls["docstring"]}"""')

        # Attributes
        for attr, typ in cls["attributes"].items():
            if typ:
                lines.append(f"    {attr}: {typ}")
            else:
                lines.append(f"    {attr}  # type: unknown")

        if not cls["attributes"] and not cls["methods"]:
            lines.append("    pass")

        # Methods
        for method_name, params, ret_type, docstring in cls["methods"]:
            param_list = []
            for name, typ, default_val in params:
                part = f"{name}: {typ}" if typ else name
                if default_val is not None:
                    part += f" = {default_val}"
                param_list.append(part)

            signature = f"(self, {', '.join(param_list)})" if param_list else "(self)"
            ret_str = f" -> {ret_type}" if ret_type else ""

            doc_lines = []
            if docstring:
                for line in docstring.splitlines():
                    doc_lines.append(f"        {line}")

            lines.append(f"    def {method_name}{signature}{ret_str}:")
            lines.append('        """')
            lines.extend(doc_lines)
            lines.append('        """')
            lines.append("        ...")

        # Write the blueprint in the same folder
        output_file = os.path.join(folder, "logicblueprint.py")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Generated {output_file}")


# Walk all component folders
for root, dirs, files in os.walk(COMPONENTS_DIR):
    for file in files:
        if file == "logic.py":
            generate_blueprint_stub(os.path.join(root, file))



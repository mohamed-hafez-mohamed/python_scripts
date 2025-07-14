import pandas as pd
from bs4 import BeautifulSoup
import re
import os

def parse_html_to_excel(html_file_path, output_excel_path):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Initialize lists to store extracted data
    functions = []
    signatures = []
    briefs = []
    parameters = []
    return_types = []

    # Find all function documentation sections
    function_sections = soup.find_all('div', class_='memproto')
    detail_sections = soup.find_all('div', class_='memdoc')

    # Process each function section
    for func_section, detail_section in zip(function_sections, detail_sections):
        # Extract function signature
        signature_text = func_section.get_text(strip=True)
        # Clean up signature to match desired format (e.g., "Std_Return Init(Config_t Config_ptr)")
        signature = re.sub(r'\s+', ' ', signature_text).strip()

        # Check if it's a valid function signature (starts with return type and has parentheses)
        if not re.match(r'^(Std_Return|void)\s+\w+\s*\(.+\)$', signature):
            continue

        # Extract function name
        func_name_match = re.search(r'\b(\w+)\s*\(', signature)
        func_name = func_name_match.group(1) if func_name_match else ''

        # Extract return type from signature
        return_type_match = re.match(r'^(Std_Return|void)\s+', signature)
        return_type = return_type_match.group(1) if return_type_match else 'None'

        # Extract brief description
        brief = 'None'
        # Look for the first paragraph that doesn't contain "Parameters" or "Returns"
        for p in detail_section.find_all('p'):
            text = p.get_text(strip=True)
            if text and not text.startswith(('Parameters', 'Returns')):
                brief = text.rstrip('.')
                break

        # Extract parameters
        param_text = 'None'
        param_table = detail_section.find('table', class_='params')
        if param_table:
            param_rows = param_table.find_all('tr')
            param_list = []
            for row in param_rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    param_name = cols[0].get_text(strip=True)
                    param_desc = cols[1].get_text(strip=True)
                    param_list.append(f"{param_name}: {param_desc}")
            param_text = '; '.join(param_list) if param_list else 'None'

        # Append extracted data to lists
        functions.append(func_name)
        signatures.append(signature)
        briefs.append(brief)
        parameters.append(param_text)
        return_types.append(return_type)

    # Create a DataFrame
    data = {
        'Function Name': functions,
        'Signature': signatures,
        'Brief Description': briefs,
        'Parameters': parameters,
        'Return Type': return_types
    }
    df = pd.DataFrame(data)

    # Export to Excel
    df.to_excel(output_excel_path, index=False, sheet_name='Function Documentation')
    print(f"Excel file generated successfully at {output_excel_path}")

if __name__ == "__main__":
    # Example usage
    current_directory = os.path.dirname(os.path.abspath(__file__))
    html_directory = current_directory + "\\html"
    html_file = os.path.join(html_directory, "_d_r_i_v_e_r__interface_8h.html") # Input HTML file 
    excel_file = os.path.join(current_directory, "functions_documentation.xlsx")   # Output Excel file
    if os.path.exists(html_file):
        parse_html_to_excel(html_file, excel_file)
    else:
        print(f"HTML file {html_file} not found.")
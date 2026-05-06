import streamlit as st

st.set_page_config(page_title="Μεταφορά Παραγωγής", layout="centered")

companies = {
    "AIG": ["B2038"],
    "Interasco": ["20719"],
    "Interamerican": ["X770101 (τυπώνω-πληρώνω)", "X770119 (ταχυπληρωμή)"],
    "Allianz Ευρωπαϊκή": ["Π1123"],
    "Expert & GMI": ["200476"],
    "Υδρόγειος": ["81803"],
    "Generali": ["13195 (τυπώνω-πληρώνω)", "13196 (ταχυπληρωμή)"],
    "Generali Ι (πρώην ΑΧΑ)": ["202206 Γενικοί", "MEDISYN 84.00.00.81 Ζωής"],
    "Intersalonica": ["67690 (γενικοί κλάδοι)", "7690 (ζωής)"],
    "ERGO": ["7155"],
    "MINETTA": ["70139"],
    "Eurolife": ["33631 (γενικοί κλάδοι)", "3631 (ζωής)"],
    "INTERLIFE": ["222-14"],
    "EUROINS": ["1835"],
    "CROMAR/LLOYD’S": ["431"],
    "GROUPAMA": ["W36828"],
    "ΑΤΛΑΝΤΙΚΗ": ["1690000002"],
    "ΕΘΝΙΚΗ": ["49664", "49868 (Protect)"],
    "ΕΥΡΩΠΗ": ["600642"],
    "KARAVIAS": ["Ρ.00383"],
    "SOUTHEASTERN": ["210965"],
    "EUROCOVER": ["664"],
    "APEIRON": ["11307"],
    "ΣΥΝΕΤΑΙΡΙΣΤΙΚΗ": ["90211"],
    "BROKINS / UNIQUE": ["07983"],
    "ARAG": ["1898/2"],
    "NNHELLAS / METLIFE": ["655-00-000"],
    "HOWDEN": ["3046"],
    "HELLAS DIRECT": ["BR00000000004764"],
    "EXTRA ASSISTANCE": ["4732"],
    "ΔΥΝΑΜΙΣ": ["D009560"],
}

st.title("Αίτημα Μεταφοράς Παραγωγής")

company = st.selectbox("Εταιρεία", list(companies.keys()))
old_code = st.selectbox("Κωδικός στην εταιρεία", companies[company])

brokers_union_code = st.text_input("Κωδικός Brokers Union")
subcode = st.text_input("Υποκωδικός", value="0000")
name = st.text_input("Ονοματεπώνυμο")

if st.button("Δημιουργία Κειμένου"):
    text = f"""Παρακαλώ για τη μεταφορά της παραγωγής μου, την οποία διατηρώ στην εταιρεία {company} με κωδικό {old_code}, στην Brokers Union με κωδικό {brokers_union_code}, στον υποκωδικό {subcode} – {name}.

Ακόμη, έχω ενημερώσει το πελατολόγιό μου τηλεφωνικά για την αλλαγή της εξυπηρέτησής τους και έχω λάβει τη συγκατάθεσή τους.

Παρακαλώ επίσης, όπως σταλεί σε μορφή Excel η συνολική μου παραγωγή για την παρακολούθηση των μεταφορών."""
    
    st.text_area("Έτοιμο κείμενο", text, height=300)
    st.download_button(
        "Κατέβασμα σε TXT",
        text,
        file_name=f"metafora_paragogis_{company}.txt",
        mime="text/plain"
    )

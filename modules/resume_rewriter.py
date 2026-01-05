def rewrite_resume(data, raw_text, country):
    header = f"""{data.get('first_name','')} {data.get('last_name','')}
EU Work Permit Candidate – {country}
Email: {data.get('email','')} | Phone: {data.get('phone','')}

"""

    summary = {
        "Luxembourg": "Operations-focused professional with hands-on experience in support, coordination, and compliance-driven environments. Seeking employer-sponsored opportunity in Luxembourg.",
        "Germany": "Detail-oriented professional with experience in structured operational environments, aligned with German workplace standards.",
        "Poland": "Reliable operations and logistics professional with experience supporting daily business workflows.",
        "Czech Republic": "Process-driven professional experienced in operational support and team coordination."
    }.get(country, "")

    skills_section = "SKILLS\n" + "\n".join(f"- {s}" for s in data.get("skills", []))

    final_resume = f"""
{header}
PROFESSIONAL SUMMARY
{summary}

{skills_section}

PROFESSIONAL EXPERIENCE
{raw_text}

EDUCATION
(As per provided details)
"""

    return final_resume.strip()

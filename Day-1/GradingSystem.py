def calculate_grade(marks):
	"""Return the letter grade for marks from 0 through 100."""
	if not 0 <= marks <= 100:
		raise ValueError("Marks must be between 0 and 100.")

	if marks >= 90:
		return "A+"
	if marks >= 80:
		return "A"
	if marks >= 70:
		return "B+"
	if marks >= 60:
		return "B"
	if marks >= 50:
		return "C"
	if marks >= 35:
		return "D"
	return "F"  


def main():
	try:
		marks = float(input("Enter marks (0-100): "))
		grade = calculate_grade(marks)
	except ValueError as error:
		print(f"Invalid input: {error}")
		return

	print(f"Grade: {grade}")


if __name__ == "__main__":
	main()

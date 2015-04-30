#include <iostream>
#include <sstream>
using namespace std;

int main() {
	// Define Strings
	string cons = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ";

	// Get Input line to Encode
	string s;
	getline(cin, s);

	// Encode Input
	stringstream sout;
	for (string::size_type i=0; i < s.size(); i++) {
		// If the character is not a consonant
		if (cons.find(s.at(i)) == string::npos) {
			// It is a vowel
			sout << s.at(i);
		} else {
			// It is a consonant
			sout << s.at(i) << "o" << static_cast<char>(tolower(s.at(i)));
		}
	}

	// Print Encoded Value
	cout << sout.str() << endl;

	return 0;
}

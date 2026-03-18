import sys
import numpy as np

from basis_utils import back_to_standard, express_in_basis, similarity_transform
from matrices import actions, bases, get_action, get_basis

ANCHOR = np.array([2.0, 2.0, 1.5], dtype=float)


def print_report(basis_name, action_name):
    basis = get_basis(basis_name)
    action = get_action(action_name)

    alien_coords = express_in_basis(ANCHOR, basis)
    recovered = back_to_standard(alien_coords, basis)
    relative_action = similarity_transform(action, basis)
    error = float(np.linalg.norm(recovered - ANCHOR))

    print("CHANGE OF BASIS REPORT")
    print("=" * 44)
    print(f"Available bases: {', '.join(bases.keys())}")
    print(f"Available actions: {', '.join(actions.keys())}")
    print(f"\nBasis: {basis_name}")
    print(f"Action: {action_name}")
    print(f"Anchor in standard coordinates: {np.round(ANCHOR, 3)}")
    print(f"Anchor in alien coordinates:    {np.round(alien_coords, 3)}")
    print(f"Round-trip error: {error:.6e}")
    print("\nRelative transform P^-1 M P:")
    for row in relative_action:
        print(f"[{row[0]:8.3f} {row[1]:8.3f} {row[2]:8.3f}]")
    print("=" * 44)


if __name__ == "__main__":
    basis_name = sys.argv[1] if len(sys.argv) > 1 else "rotated_z45"
    action_name = sys.argv[2] if len(sys.argv) > 2 else "scale2x"
    print_report(basis_name, action_name)

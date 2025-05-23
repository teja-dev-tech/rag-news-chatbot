import { Github } from 'lucide-react';

export default function GithubLink() {
  return (
    <a 
      href="https://github.com/yourusername" 
      target="_blank" 
      rel="noopener noreferrer"
      className="fixed top-4 right-4 p-2 rounded-full bg-gray-100 hover:bg-gray-200 transition-colors shadow-sm"
      aria-label="GitHub Profile"
      title="View on GitHub"
    >
      <Github className="w-6 h-6 text-gray-800" />
    </a>
  );
}
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, Loader2 } from 'lucide-react';

export default function ArticlesPage() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/articles');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setArticles(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error('Error fetching articles:', err);
        setError(err.message || 'Failed to load articles');
      } finally {
        setLoading(false);
      }
    };

    fetchArticles();
  }, []);

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen">
        <Loader2 className="w-8 h-8 animate-spin text-[#0c7ff2] mb-4" />
        <p className="text-[#121416]">Loading articles...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="px-40 py-10">
        <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded">
          <div className="flex">
            <div className="flex-shrink-0">
              <svg className="h-5 w-5 text-red-500" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
              </svg>
            </div>
            <div className="ml-3">
              <p className="text-sm text-red-700">Error: {error}</p>
            </div>
          </div>
        </div>
        <div className="mt-6">
          <Link to="/" className=" no-underline inline-flex items-center text-[#0c7ff2] hover:text-[#0a6bd9] font-medium">
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Chat
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="px-40 py-10 text-left">
      <div className="mt-8 text-center">
        <Link to="/" className="no-underline inline-flex items-center text-[#0c7ff2] hover:text-[#0a6bd9] font-medium">
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back to Chat
        </Link>
      </div>
      <div className="flex flex-wrap justify-between gap-3 p-4">
        <h1 className="text-[#121416] tracking-light text-[32px] font-bold leading-tight min-w-72">Articles</h1>
      </div>
      
      <div className="space-y-6">
        {articles.length === 0 ? (
          <div className="text-center py-12 bg-white rounded-xl">
            <p className="text-[#6a7681]">No articles found.</p>
          </div>
        ) : (
          articles.map((article, index) => (
            <div key={article.id || index} className="p-4">
                <div className="flex flex-col gap-3 rounded-xl hover:bg-gray-50 transition-colors p-4">
                  <h2 className="text-[#121416] text-base font-bold leading-tight">
                    {article.title || 'Untitled Article'}
                  </h2>
                  {article.description && (
                    <p className="text-[#6a7681] text-sm font-normal leading-normal line-clamp-3">
                      {article.description}
                    </p>
                  )}
                  <div className="flex items-center mt-1">
                    {article.source_domain && (
                      <span className="text-xs text-[#6a7681] bg-gray-100 px-2 py-1 rounded-full">
                        {article.source_domain}
                      </span>
                    )}
                    <span style={{ whiteSpace: 'pre' }}>   </span>
                    {article.date_publish && (
                      <span className="text-xs text-[#6a7681] ml-2">
                        {new Date(article.date_publish).toLocaleDateString()}
                      </span>
                    )}
                  </div>
                </div>
              
              {article.url && (
                <div className="mt-2 flex justify-end">
                  <a
                    href={article.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center text-sm text-[#0c7ff2] hover:text-[#0a6bd9] font-medium"
                    title="Read full article"
                  >
                    Read more
                  </a>
                </div>
              )}
            </div>
          ))
        )}
      </div>
        
     
    </div>
  );
}
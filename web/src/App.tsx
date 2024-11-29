import { useCallback, useMemo, useState } from 'react'
import './App.css'
import $http from './utils/http'

function App() {
  const [path, setPath] = useState('')
  const [keyword, setKeyword] = useState('')
  const [images, setImages] = useState([])

  const handleAddDir = useCallback(() => {
    $http.post('/images/add', { dir: path })
  }, [path])

  const handleSearch = useCallback(async () => {
    const res = await $http.get('/images/search', { params: { keyword } })

    setImages(res.data[0].sort((a,b) => b.distance - a.distance).map(item =>  ({
      path: 'http://127.0.0.1:37679/images?path=' + item.entity.path,
      distance: item.distance
    })))
  }, [keyword])

  return (
<div>
<div>
      <input type="text" value={path} onChange={e => setPath(e.target.value)} />
      <button onClick={handleAddDir}>Add</button>
    </div>
        <div>
        <input type="text" value={keyword} onChange={e => setKeyword(e.target.value)} />
        <button onClick={handleSearch}>Search</button>
      </div>
      <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center', gap: 12}}>
        {
          images.map(item => {
            return <div>
              <img key={item.path} src={item.path} width="auto" height={200}></img>
              <center>{item.distance}</center>
            </div>
          })
        }
      </div>
</div>
  )
}

export default App
